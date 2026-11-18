# Milestone 5 — Database and checkout

Design SQLAlchemy models: products, causes, orders, order_items and contributions. For each, decide columns, types, primary keys and foreign keys. Store money in cents, and snapshot price and allocation rates at checkout. Use Flask-Migrate to initialize and apply migrations (see RUNNING). Create repeatable seed data. Query products from SQLite, enable foreign key enforcement, and use ORM queries or parameterized SQL.

Build simulated checkout: validate nonempty cart and cause on server, calculate totals, save order/items/contribution in one transaction, roll back on failure, clear cart only after success and show confirmation. Prevent accidental duplicate checkout. No payments, passwords or personal data required. Write SQL queries for order count, sales and contributions by cause. Inspect saved records using DB Browser if desired.

Before moving on: completed purchases persist after restarting locally, failed checkout leaves no partial order, queries work. Commit and push.
