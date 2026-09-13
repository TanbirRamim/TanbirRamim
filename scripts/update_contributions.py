#!/usr/bin/env python3
"""Refresh the open source contributions section of README.md.

Lists recent pull requests by the profile owner to public projects owned by someone else with at
least MIN_STARS stars, merged ones first. Standard library only; needs GITHUB_TOKEN.
"""

from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

USER = "TanbirRamim"
MIN_STARS = 500
LIMIT = 25
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- CONTRIBUTIONS:START -->", "<!-- CONTRIBUTIONS:END -->"


def api(url: str) -> dict:
    request = urllib.request.Request(url)
    request.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("User-Agent", f"{USER}-profile-readme")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_pull_requests() -> list[dict]:
    query = urllib.parse.quote(f"author:{USER} is:pr is:public -user:{USER}")
    items = api(f"https://api.github.com/search/issues?q={query}&sort=created&order=desc&per_page=100")["items"]
    stars: dict[str, int] = {}
    results = []
    for item in items:
        repo = item["repository_url"].removeprefix("https://api.github.com/repos/")
        if repo not in stars:
            stars[repo] = api(item["repository_url"])["stargazers_count"]
        merged = bool(item.get("pull_request", {}).get("merged_at"))
        if stars[repo] < MIN_STARS or (item["state"] == "closed" and not merged):
            continue
        results.append({"repo": repo, "stars": stars[repo], "url": item["html_url"],
                        "number": item["number"], "title": item["title"], "merged": merged})
    return results


def stars_label(stars: int) -> str:
    return f"{stars / 1000:.1f}k".replace(".0k", "k") if stars >= 1000 else str(stars)


def render(pull_requests: list[dict]) -> str:
    if not pull_requests:
        return "No public contributions to list yet."
    projects: dict[str, list[dict]] = {}
    for pr in pull_requests:
        projects.setdefault(pr["repo"], []).append(pr)
    ordered = sorted(projects.items(), key=lambda entry: entry[1][0]["stars"], reverse=True)[:LIMIT]
    merged_total = sum(pr["merged"] for pr in pull_requests)
    review_total = len(pull_requests) - merged_total
    lines = [
        f"**{len(pull_requests)}** pull requests to **{len(projects)}** open source projects: "
        f"**{merged_total}** merged, **{review_total}** in review. Updated daily by a GitHub Action.",
        "",
        "| Project | Stars | Pull requests |",
        "| --- | ---: | --- |",
    ]
    for repo, prs in ordered:
        prs.sort(key=lambda pr: (not pr["merged"], -pr["number"]))
        links = "<br>".join(
            f"{'🟣' if pr['merged'] else '🟢'} [{pr['title'].replace('|', '&#124;').replace('<', '&lt;')}]({pr['url']})"
            for pr in prs
        )
        lines.append(f"| [{repo}](https://github.com/{repo}) | {stars_label(prs[0]['stars'])} | {links} |")
    lines += ["", "🟣 merged &nbsp; 🟢 in review"]
    return "\n".join(lines)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    block = f"{START}\n{render(fetch_pull_requests())}\n{END}"
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.DOTALL)
    README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
