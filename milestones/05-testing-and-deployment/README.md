# Milestone 5: Testing and Deployment

[← Project overview](../../README.md)

## Goal

Make sure the application works and share it with someone else.

## Your tasks

- Test a normal cart, an empty cart, an invalid quantity, a saved order and the dashboard totals.
- Install Pytest if needed (`uv add --dev pytest`). Write at least two automated tests for your financial functions, including an invalid input or rounding case. Run `uv run pytest`.
- Fix problems you find and record anything you could not finish.
- Deploy using PythonAnywhere or Render with your mentor’s guidance. Disable debug mode, configure secrets outside code and check whether SQLite storage persists on your hosting plan. If storage resets, document that and provide a demo seed script.
- Add screenshots, the live URL, setup notes and a short reflection to your README. Label all transactions as simulated.
- Record a short screen demonstration explaining what you built and one challenge you solved.

## Before you move on

Your tests run, you have checked the deployed URL in a browser, and another person can understand the project from your README. Report any failed tests or deployment limitations honestly.

## Submit your work

Share your repository, live URL, screenshots, test results and short demo with your mentor.

Follow the [development workflow](../../README.md#development-workflow): move the Jira task to In Progress, create a branch from your fork's main, commit and push your changes, and open a pull request against your fork's main for mentor review. Link the issue and Jira task. Move the task to Done after approval and merge.

## Helpful resources

[Pytest](https://docs.pytest.org/) · [PythonAnywhere](https://www.pythonanywhere.com/) · [Render Flask deployment](https://render.com/docs/deploy-flask)
