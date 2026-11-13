# Repository Guide

## Structure and architecture

`viikko2/` contains independent Python exercises; use each subdirectory as its own `uv` project and keep its dependencies in that project's `pyproject.toml` and `uv.lock`.

In `viikko2/nhl-reader`, `src/index.py` is the entry point. It passes a URL to `PlayerReader`, which fetches the NHL player JSON and creates `Player` objects; `PlayerStats` consumes the reader and filters or ranks those players. Keep fetching, player data, and statistics in their respective modules.

`viikko2/uv-web` is a separate project with FastAPI and SQLAlchemy dependencies.

## Build, test, and lint

Run commands from the repository root unless a command changes directory:

- Sync a project's dependencies with `uv sync --project viikko2/nhl-reader` or `uv sync --project viikko2/uv-web`.
- Lint the NHL reader with `cd viikko2/nhl-reader && uv run pylint src/index.py src/player.py src/player_reader.py src/player_stats.py`.
- Run the `uv-web` tests with `uv run --project viikko2/uv-web pytest`.
- Run one test with `uv run --project viikko2/uv-web pytest tests/test_file.py::test_name`.

## Conventions

- Each project has its own Python environment and lockfile; run tools against the project being changed.
- The NHL reader uses simple modules in `src/` with direct imports between them. `PlayerStats` receives a reader instance rather than performing HTTP requests itself.
- Both projects currently require Python 3.14 or newer; preserve their declared runtime constraints when changing dependencies.
