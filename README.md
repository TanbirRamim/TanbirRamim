<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Tanbir Hossain Ramim. Software engineer, moving into AI engineering." width="100%">
</picture>

<p>
  <a href="https://www.tanbirramim.com"><img alt="Website" src="https://img.shields.io/badge/tanbirramim.com-0E7C72?style=for-the-badge&logo=googlechrome&logoColor=white"></a>
  <a href="mailto:contact.tanbirramim@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-13263A?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <img alt="Open to AI and software engineering roles" src="https://img.shields.io/badge/Open_to-AI_%2F_SWE_roles-C2710C?style=for-the-badge">
  <img alt="Location" src="https://img.shields.io/badge/Regensburg,_Germany-4A5F74?style=for-the-badge&logo=googlemaps&logoColor=white">
</p>

I'm a software engineer in Regensburg, studying Computer Science at **OTH Regensburg** and moving from full-stack work into **AI engineering**. I like problems where the constraint is the interesting part: training compute, voice latency, paperwork that software should have absorbed years ago.

Open to working student, internship and part-time roles in Germany and the EU, and to remote collaboration.

## What I'm building

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>⚡ <a href="https://enai-lab.com">EnAi</a></h3>
      Cuts neural network training compute <b>while the model is still training</b>. It watches gradient energy per layer, freezes layers whose contribution has collapsed, and moves the freed headroom into larger batches, with no restart and no model code changes.
      <br><br>
      <b>6.91%</b> training compute removed<br>
      <b>+20.9%</b> throughput once engaged<br>
      <sub>PyTorch · autograd hooks · Apple Silicon (MPS)</sub>
    </td>
    <td width="33%" valign="top">
      <h3>🎓 Phoveus Lab</h3>
      A small collective building AI products that ship free and open source. The first is <b>Admission OPS</b>: university admissions is one of the most paperwork-heavy moments in a person's life, and most of it is deadline tracking that software should handle.
      <br><br>
      <sub>Next.js · TypeScript · Python · LLM orchestration · Postgres</sub>
    </td>
    <td width="33%" valign="top">
      <h3>📡 <a href="https://github.com/TanbirRamim/open-source-radar">Open Source Radar</a></h3>
      Finds open source issues people can actually start today: unclaimed, beginner-friendly issues from 1,200+ active projects in 30 languages, with each project's CLA and AI-policy rules shown up front. Refreshed twice a day.
      <br><br>
      <a href="https://tanbirramim.github.io/open-source-radar/">Browse issues</a> · <a href="https://github.com/TanbirRamim/open-source-radar/tree/main/guide">Read the guide</a><br>
      <sub>Python · GitHub Actions · GraphQL API</sub>
    </td>
  </tr>
</table>

## Open source contributions

<!-- CONTRIBUTIONS:START -->
**17** pull requests to **15** open source projects: **0** merged, **17** in review. Updated daily by a GitHub Action.

| Project | Stars | Pull requests |
| --- | ---: | --- |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | 35.4k | 🟢 [fix: give tabs created in a detached session a real size](https://github.com/zellij-org/zellij/pull/5612) |
| [fyne-io/fyne](https://github.com/fyne-io/fyne) | 28.7k | 🟢 [Fix selection position in center and trailing aligned labels](https://github.com/fyne-io/fyne/pull/6534) |
| [OpenAPITools/openapi-generator](https://github.com/OpenAPITools/openapi-generator) | 26.7k | 🟢 [[kotlin] Fix inline enum array parameter default values](https://github.com/OpenAPITools/openapi-generator/pull/24940) |
| [uutils/coreutils](https://github.com/uutils/coreutils) | 24.1k | 🟢 [tr: do not expand [c*n] repeats character by character](https://github.com/uutils/coreutils/pull/14524)<br>🟢 [date: treat blank lines in --file input as midnight today](https://github.com/uutils/coreutils/pull/14523)<br>🟢 [df: round the total row once, from the summed bytes](https://github.com/uutils/coreutils/pull/14522) |
| [JanDeDobbeleer/oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh) | 23.5k | 🟢 [fix(language): read custom tools from YAML configs](https://github.com/JanDeDobbeleer/oh-my-posh/pull/7870) |
| [svg/svgo](https://github.com/svg/svgo) | 22.7k | 🟢 [fix(removeUselessDefs): keep animations that target elements by href](https://github.com/svg/svgo/pull/2292) |
| [npm/cli](https://github.com/npm/cli) | 10.1k | 🟢 [fix: allow email usernames when logging in to custom registries](https://github.com/npm/cli/pull/9967) |
| [taskforcesh/bullmq](https://github.com/taskforcesh/bullmq) | 9.4k | 🟢 [fix(worker): trace stalled checks independently of startStalledCheckTimer span](https://github.com/taskforcesh/bullmq/pull/4736) |
| [oapi-codegen/oapi-codegen](https://github.com/oapi-codegen/oapi-codegen) | 8.6k | 🟢 [fix(strict-server): delegate JSON marshalling for allOf unions and additionalProperties](https://github.com/oapi-codegen/oapi-codegen/pull/2552) |
| [raphamorim/rio](https://github.com/raphamorim/rio) | 7.5k | 🟢 [rioterm: use vi-cursor color while in Vi mode](https://github.com/raphamorim/rio/pull/1932) |
| [aiogram/aiogram](https://github.com/aiogram/aiogram) | 5.9k | 🟢 [Fix ephemeral reply addressed to the bot instead of receiver_user](https://github.com/aiogram/aiogram/pull/1911) |
| [pmd/pmd](https://github.com/pmd/pmd) | 5.5k | 🟢 [[java] Fix #7063: CheckResultSet false positive with next() as ternary condition](https://github.com/pmd/pmd/pull/7066) |
| [aws-powertools/powertools-lambda-python](https://github.com/aws-powertools/powertools-lambda-python) | 3.3k | 🟢 [fix(event_handler): match generic alias response models in OpenAPI schema](https://github.com/aws-powertools/powertools-lambda-python/pull/8453) |
| [testing-library/user-event](https://github.com/testing-library/user-event) | 2.3k | 🟢 [fix: track value of inputs and textareas in shadow DOM](https://github.com/testing-library/user-event/pull/1332) |
| [python-rope/rope](https://github.com/python-rope/rope) | 2.2k | 🟢 [Treat type alias statements as name assignments](https://github.com/python-rope/rope/pull/874) |

🟣 merged &nbsp; 🟢 in review
<!-- CONTRIBUTIONS:END -->

## Experience

| Role | Where | When |
| --- | --- | --- |
| **Student Assistant**. Built the real-time voice negotiation simulator Sales Management students train against, then re-architected it for concurrent sessions across courses. | OTH Regensburg | 2025 to now |
| **Co-Founder**. Client acquisition and the technical delivery behind it, plus tooling that removed the manual steps between brief and handover. | Softwarence | 2024 to now |
| **Working Student, Web & Digital**. Rebuilt the property websites and shipped booking, food ordering and venue reservation flows, plus the internal operations platform. | Birnbaum Hotels | 2025 to 2026 |
| **Web Application Developer**. Mobile-first web apps in React and Tailwind, integrating REST APIs from wireframe to production. | Dongyi Sourcing UK | 2022 to 2023 |
| **Intern**. Frontend features, API integration, bug fixing and UI testing. | Nilecode | 2022 |

Full details on [tanbirramim.com](https://www.tanbirramim.com).

## Stack

<p>
  <img alt="Python, PyTorch, TypeScript, JavaScript, React, Next.js, Node.js, PostgreSQL, AWS, Docker, Rust, C++, Java, Linux, Git" src="https://skillicons.dev/icons?i=py,pytorch,ts,js,react,nextjs,nodejs,postgres,aws,docker,rust,cpp,java,linux,git&perline=15">
</p>

**Weekly:** Python, PyTorch, TypeScript, Next.js, Node.js, PostgreSQL, WebRTC and streaming audio, OpenAI APIs, RAG and agents.<br>
**Also:** FastAPI, Spring Boot, LangChain and LangGraph, vector databases, Docker, GitHub Actions, Rust, C++.

## Background

My first program was in C, out of one chapter of a college ICT syllabus in Dhaka. I found it more interesting than the rest of the syllabus combined, which led to competitive programming, then to teaching: my [Data Structures and Algorithms](https://github.com/TanbirRamim/DataStructureAndAlgorithms) repository pairs code in several languages with video walkthroughs of the classic algorithms. Today that curiosity goes into training efficiency, real-time voice systems and open source.

<p align="center">
  <img alt="Profile views" src="https://komarev.com/ghpvc/?username=tanbirramim&label=Profile%20views&color=0E7C72&style=flat">
</p>
