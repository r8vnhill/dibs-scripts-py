"""
Utility for validating directory paths in argparse.
"""

import argparse
from pathlib import Path


def validated_directory(value: str) -> Path:
    """Validate that a string represents a valid directory path.

    Args:
        value: String path to validate.

    Returns:
        Path object if the directory exists.

    Raises:
        argparse.ArgumentTypeError: If the path is not a valid directory.
    """
    p = Path(value)
    if not p.is_dir():
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid directory")
    return p
