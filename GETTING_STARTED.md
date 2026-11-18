# Getting started

## Day 1 checklist
- [ ] Create a GitHub account and apply for [student benefits](https://github.com/settings/education/benefits) using your university enrollment evidence. Do not wait for approval to begin.
- [ ] Install [Python](https://www.python.org/downloads/), [VS Code](https://code.visualstudio.com/), [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/getting-started/installation/). [DB Browser for SQLite](https://sqlitebrowser.org/) is optional. SQLite needs no separate server.
- [ ] Fork this repository and clone your fork.
- [ ] Read the requirements and explain the business model in your own words.
- [ ] Run the starter, personalize its welcome page, commit and push.

```sh
git clone https://github.com/YOUR-USERNAME/stellafy-starter.git
cd stellafy-starter
uv sync
```
Use your actual repository name if you renamed the fork. Python 3.12 is recommended; uv can install it with `uv python install 3.12`.

Copy `.env.example` to `.env` (PowerShell: `Copy-Item .env.example .env`; macOS/Linux: `cp .env.example .env`). Generate a random secret with `uv run python -c "import secrets; print(secrets.token_hex(32))"` and put the result in `.env`. Never commit that file.

```sh
uv run flask --app run run --debug
```
Open http://127.0.0.1:5000. Stop the server with Ctrl+C. Run `uv run pytest` to check the starter. Commit the generated `uv.lock` file after syncing.
