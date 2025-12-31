"""Generate a README.md file from simple CLI parameters.

Examples:
    Write a README into the current directory with verbose logging::

        uv run -m readme_gen.new_readme --name "My Project" --verbose

    Write into a specific folder::

        uv run -m readme_gen.new_readme --name "My Project" --out_dir docs
"""

from datetime import datetime
from pathlib import Path
import sys

from readme_gen.app_logging import setup_logging
from readme_gen.parser import build_parser


def write_readme(content: str, out_dir: Path) -> None:
    """Write README content to ``README.md`` in the given directory.

    Args:
        content: Markdown content to persist.
        out_dir: Target directory where the README should be written.

    Returns:
        None

    Raises:
        OSError: If the file cannot be written.

    Examples:
        >>> from pathlib import Path
        >>> write_readme("# Title\n", Path("."))
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "README.md"
    with target.open("w", encoding="utf-8") as f:
        f.write(content)


def main(argv: list[str]) -> int:
    """Parse CLI args, render README content, and write it to disk.

    Args:
        argv: Argument vector (typically ``sys.argv[1:]``).

    Returns:
        Exit code integer; 0 on success.

    Examples:
        >>> main(["--name", "Demo"])
        0
    """
    args = build_parser().parse_args(argv)
    logger = setup_logging(args.verbose)
    logger.info("Creating README.md for project '%s'", args.name)

    content = (
        f"# {args.name}\n\n"
        f"Project initialized on {datetime.now():%Y-%m-%d %H:%M:%S}.\n\n"
        "Learn more about READMEs at https://www.makeareadme.com/.\n"
    )

    write_readme(content, args.out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
