# Milestone 6 — Analytics

Install analytics dependencies with `uv sync --group analytics` (and use the same group on the deployment host if needed).

Generate at least 30 fictional transactions with a reproducible script (fixed random seed or deterministic rows). Label the data simulated. Use SQL and Pandas for total sales, order count, commissions, contributions, retained revenue and average order value (handle zero orders). Avoid double-counting when joining line items. Use Chart.js for contributions by cause and sales over time.

Verify three metrics manually. Answer with actual simulated figures: which cause receives most, which category sells most, what is average order value, how do allocation rates affect retained revenue, and what expenses would you need to know to measure profit?

Before moving on: two charts and accurate metrics derived from the database. Commit and push. If time is tight, start with SQL totals and one chart, documenting the rest as unfinished.
