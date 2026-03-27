"""Utilities for persisting JSON-compatible values used by the structured-output examples.

This module defines the recursive value model accepted by the local JSON-writing helpers and keeps
the file-output policy in one place so nearby scripts produce consistent artifacts.

The goal is intentionally narrow: represent values that can be serialized by the standard-library
:mod:`json` module without custom encoders and write them using a stable, readable formatting
policy.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypeAlias

JSONValue: TypeAlias = (
    dict[str, "JSONValue"] | list["JSONValue"] | str | int | float | bool | None
)
"""Recursive alias for JSON-serializable values with string keys for objects.

The alias mirrors the subset of Python values that maps naturally to JSON in this example:

- ``dict[str, JSONValue]`` for JSON objects
- ``list[JSONValue]`` for JSON arrays
- ``str``, ``int``, ``float``, ``bool``, and ``None`` for scalar values

This alias is recursive because JSON objects and arrays may contain nested objects and arrays.
"""


def save_to_json(data: JSONValue, filename: str | Path) -> None:
    """Write a JSON-compatible value to disk using a stable text format.

    The file is written as UTF-8, preserves non-ASCII characters directly, uses indentation for
    readability, and sorts object keys so repeated writes are easier to compare in examples, tests,
    and version control.

    :param data:
        JSON-compatible value to serialize.
    :param filename:
        Destination path for the JSON file. Accepts either a string path or a :class:`pathlib.Path`.
    """

    with Path(filename).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
