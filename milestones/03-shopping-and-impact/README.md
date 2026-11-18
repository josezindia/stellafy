# Milestone 3: Shopping and Social Impact

[← Project overview](../../README.md) | [Next milestone →](../04-database-and-analytics/README.md)

## Goal

Turn the storefront into a simulated shopping experience.

## Your tasks

- Add a shopping cart using a Flask session. Let customers add or remove products and view their total. Configure a secret key outside source code.
- Let the customer select a cause. Start with normal HTML forms; try HTMX to update the cart without reloading the whole page once the forms work.
- Write Python functions `calculate_commission()` and `calculate_contribution()`. Use integer cents or Decimal for money and round consistently.
- Show an order summary with the purchase total, commission, cause contribution and platform revenue before expenses.
- Reject invalid product IDs, quantities and missing causes on the server. Do not accept prices supplied by the browser as authoritative.
- Add a simulated checkout confirmation. Saving orders permanently comes in the next milestone. Do not collect real payments.

## Before you move on

Adding $25 and $15 products gives a $40 total. A $100 purchase at 10% commission and 60% cause allocation gives $10 commission, $6 contribution and $4 platform revenue. Removing an item updates the total; invalid inputs do not crash the app.

## Submit your work

Attach a screenshot of the cart and explain how you tested the calculation.

Follow the [development workflow](../../README.md#development-workflow): move the Jira task to In Progress, create a branch from your fork's main, commit and push your changes, and open a pull request against your fork's main for mentor review. Link the issue and Jira task. Move the task to Done after approval and merge.

## Helpful resources

[Flask sessions](https://flask.palletsprojects.com/en/stable/quickstart/#sessions) · [HTMX documentation](https://htmx.org/docs/)
