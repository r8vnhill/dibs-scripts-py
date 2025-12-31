from datetime import datetime
from pathlib import Path
import sys

from readme_gen.app_logging import setup_logging
from readme_gen.parser import build_parser




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
