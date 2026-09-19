"""Console entry point for the CLI application."""

from collections.abc import Sequence

from template_python_cli.commands.example import run_example_command
from template_python_cli.exceptions import TemplatePythonCliError


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line application."""
    try:
        # TODO: Implement CLI argument handling.
        run_example_command(argv)
    except TemplatePythonCliError:
        # TODO: Implement error-to-exit-code handling.
        raise
    return 0
