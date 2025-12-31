import argparse
import logging
from datetime import datetime
from pathlib import Path
import sys


def validated_directory(value: str) -> Path:
    p = Path(value)
    if not p.is_dir():
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid directory")
    return p


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    p.add_argument("-v", "--verbose", action="store_true")
    p.add_argument("-o", "--out_dir", type=validated_directory, default=".")
    return p


def setup_logging(verbose: bool) -> logging.Logger:
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(level=level, format="%(message)s")
    return logging.getLogger(__name__)


def write_readme(content: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "README.md"
    with target.open("w", encoding="utf-8") as f:
        f.write(content)


def main(argv: list[str]) -> int:
    p = build_parser()
    args = p.parse_args(argv)
    log = setup_logging(args.verbose)
    log.info("Creating README.md for project '%s'", args.name)

    content = (
        f"# {args.name}\n\n"
        f"Project initialized on {datetime.now():%Y-%m-%d %H:%M:%S}.\n\n"
        "Learn more about READMEs at https://www.makeareadme.com/.\n"
    )

    write_readme(content, args.out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
