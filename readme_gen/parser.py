"""Command-line argument parser for the README generator."""

import argparse

from readme_gen.validated_directory import validated_directory


def build_parser() -> argparse.ArgumentParser:
    """Build and configure the argument parser for readme-gen.

    Returns:
        Configured ArgumentParser with all required and optional arguments.
    """
    p = argparse.ArgumentParser(
        prog="readme-gen",
        description="Generate a README.md from simple parameters.",
    )

    p.add_argument(
        "--name",
        required=True,
        help="Project name (used in the README title and sections).",
    )

    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output (extra messages during execution).",
    )

    p.add_argument(
        "-o",
        "--out_dir",
        type=validated_directory,
        default=".",
        help="Directory where README.md will be written (default: current directory).",
    )

    return p
