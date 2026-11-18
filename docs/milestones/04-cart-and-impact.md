# Milestone 4 — Cart and impact

Store product IDs and quantities in the Flask session; look up prices on the server. Add, remove and update items. Reject invalid quantities and unknown products. Add cause selection and show the contribution breakdown. First make ordinary forms work; then use HTMX to refresh the cart fragment. Use POST for changes and CSRF protection before publishing interactive forms.

Implement a pure function in `app/services/impact.py`: commission = total × rate; contribution = commission × cause share; retained revenue = commission − contribution. Use integer cents or Decimal with documented rounding. Reject negative totals and rates outside 0–100%. Test $100/10%/60% → $6 contribution, $50/10%/60% → $3, $200/8%/50% → $8 and $0 → $0. Explain why sales are different from retained revenue.

Before moving on: cart works, calculations match manual examples and bad input is handled. Commit and push.
