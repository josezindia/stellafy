# Milestone 7 — Testing and deployment

Use pytest for impact calculations, zero and negative amounts, invalid rates, rounding and balance. Test cart changes, invalid input and successful/failed checkout. Run `uv run pytest`. Record expected versus actual for all five acceptance criteria; failures are findings to document and fix.

Deploy using [PythonAnywhere](https://www.pythonanywhere.com/) or [Render](https://render.com/). Verify current plan limitations and Python support before choosing. GitHub Pages cannot run Flask. Render free web services have ephemeral storage; use reproducible seed data or a persistent host. Do not promise persistent orders on ephemeral storage. Use compiled Tailwind/custom CSS, set a secret through host configuration, disable debug, use a production WSGI server and protect state-changing forms against CSRF. No real payments or sensitive data. If hosting is blocked, record a local demo instead.

Complete README and [submission checklist](../SUBMISSION.md). Commit and push. Explain one design choice, one bug and one limitation you encountered.
