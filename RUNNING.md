# Running and troubleshooting

| Task | Command |
|---|---|
| Sync dependencies | `uv sync` |
| Start local server | `uv run flask --app run run --debug` |
| Run tests | `uv run pytest` |
| Add dependency | `uv add PACKAGE` |
| Initialize migrations (once, after models exist) | `uv run flask --app run db init` |
| Generate migration | `uv run flask --app run db migrate -m "Describe change"` |
| Apply migration | `uv run flask --app run db upgrade` |

Review generated migrations before applying them. Commit migrations, not the SQLite database. If a command fails, record the exact command and error; check that you are in the repository root and ran `uv sync`. If port 5000 is busy, add `--port 5001`. Never use debug mode on a public host.
