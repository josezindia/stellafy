# Milestone 1: Getting Started

[← Project overview](../../README.md) | [Next milestone →](../02-storefront/README.md)

## Goal

Get your computer ready and run a small Flask website. You do not need to understand every file yet.

## Your tasks

- Follow the [environment setup](../../README.md#environment-setup). Apply for GitHub student benefits and accept your Jira invitation.
- Open your fork in VS Code and check `git --version`, `python --version` (or `python3 --version`) and `uv --version` in the terminal.
- If the starter files exist, run `uv sync` and follow the main README to start the app. Otherwise, initialize the project with `uv init --bare` (only if there is no `pyproject.toml`) and `uv add flask`. Create `app/__init__.py` with a Flask application factory and `run.py` to create and run the app. Use the Flask quickstart as a guide.
- Create a `.gitignore` that excludes `.venv/`, `.env`, `__pycache__/` and `instance/`. Keep secrets out of GitHub.
- Make the homepage display “Welcome to Stellafy — Small purchases. Brighter futures.”
- In your own words, explain how Stellafy helps customers support a cause without paying extra.

## Before you move on

Your website opens at http://127.0.0.1:5000 when you run `uv run python run.py`. You can explain what Flask does and what Stellafy is trying to solve.

## Submit your work

Attach a screenshot of the running website to your assigned GitHub issue.

Follow the [development workflow](../../README.md#development-workflow): move the Jira task to In Progress, create a branch from your fork's main, commit and push your changes, and open a pull request against your fork's main for mentor review. Link the issue and Jira task. Move the task to Done after approval and merge.

## Helpful resources

[Flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) · [uv guide](https://docs.astral.sh/uv/)
