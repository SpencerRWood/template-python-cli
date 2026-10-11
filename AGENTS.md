# Repository Guidance

## Purpose and boundaries
- Keep this `argparse` CLI baseline reusable after package and command rename.
- Leave domain commands and external integrations to the cloned project.

## Development
- Keep `src/` entry points small and return stable exit codes.
- Test command behavior and help output without requiring network access.

## Validation
- Run `uv sync --frozen --group dev`, `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy`, `uv run pytest`, and `uv run pre-commit run --all-files`.
- Run `uv build` when entry point or package metadata changes.

## Architecture constraints
- Update the project script, package path, tests, and README together when renaming.
- Avoid adding a project-specific command to the reusable baseline.

## Safety
- Keep example arguments and fixtures free of hostnames, credentials, and local paths.

## Branching strategy

- This repository uses **trunk-based development**. Create short-lived change branches from current `main` and target PRs to `main`.
- Follow the [canonical branching and delivery policy](https://github.com/SpencerRWood/codex-config/blob/main/docs/branching-policy.md), available through the installed codex-config source path. Verify the strategy, release association, fetched base and PR target before implementation and record them in Story evidence. Story completion does not authorize publication or deployment; retain existing review, CI, security and rollback requirements.
- This classification applies to maintenance of the template repository. Replace it with the new repository's classification during project creation; applications must use release-branch integration before Story development begins.
