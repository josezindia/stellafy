# Milestone 4: Database and Analytics

[← Project overview](../../README.md) | [Next milestone →](../05-testing-and-deployment/README.md)

## Goal

Save simulated orders and use them to understand the business.

## Your tasks

- Install Flask-SQLAlchemy with `uv add flask-sqlalchemy` if it is not already installed.
- In `app/models.py`, design simple models for products, causes and orders. Each order should record the selected cause, purchase total, commission, contribution, platform share and date. Add order items if your cart needs them.
- Initialize SQLite and make sure the generated database is ignored by Git. Use Flask-Migrate if your mentor assigns migrations.
- Save each completed simulated order and clear the cart only after the save succeeds.
- Create at least 20 fictional orders using a small seed script. Label the data as simulated.
- Build a dashboard showing total sales, number of orders, contributions and platform revenue before expenses. Use SQLAlchemy queries or SQL; try Pandas or a Chart.js chart if time allows.

## Before you move on

An order remains available after restarting locally. The dashboard totals agree with the stored orders, and total commission equals contributions plus platform revenue. You can explain the difference between sales and platform revenue.

## Submit your work

Attach a dashboard screenshot and show how you checked one total against the database.

Follow the [development workflow](../../README.md#development-workflow): move the Jira task to In Progress, create a branch from your fork's main, commit and push your changes, and open a pull request against your fork's main for mentor review. Link the issue and Jira task. Move the task to Done after approval and merge.

## Helpful resources

[Flask-SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/) · [SQLite](https://sqlite.org/docs.html) · [Chart.js](https://www.chartjs.org/docs/latest/)
