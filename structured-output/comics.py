"""Comic model and JSON conversion helpers for the structured-output examples.

This module marks the point where loosely structured external JSON stops being treated as an
arbitrary mapping and becomes an explicit program-facing model.

In the surrounding examples, JSON acts as an interchange format at the script boundary, while
:class:`Comic` represents the trusted internal shape consumed by the rest of the program.
"""

from dataclasses import dataclass
import json
from pathlib import Path

from json_utils import JSONValue


@dataclass(frozen=True)
class Comic:
    """Small immutable model for the sample comic payload.

    The class gives a stable name and field structure to data that would otherwise remain a generic
    ``dict``. Using a dataclass makes the expected shape explicit and provides generated helpers
    such as ``__init__`` and ``__repr__``.

    :param title: Comic title.
    :type title: str
    :param writer: Primary writer associated with the comic.
    :type writer: str
    :param release_year: Publication year used by the sample JSON payload.
    :type release_year: int
    """

    title: str
    writer: str
    release_year: int

    def to_json_serializable(self) -> JSONValue:
        """Return this instance as a JSON-compatible object.

        The returned value is a ``dict`` keyed by the dataclass field names, so it can be serialized
        directly with :func:`json.dump` in this example.

        This implementation relies on ``self.__dict__`` because all fields are already simple
        JSON-compatible scalars. For richer models containing nested objects, dates, enums, or other
        non-JSON-native values, each field would need explicit conversion before serialization.

        :returns: JSON-compatible representation of this comic.
        :rtype: JSONValue
        """

        return self.__dict__


def comic_from_json(file_path: str | Path) -> Comic:
    """Load a :class:`Comic` from a JSON file.

    The file is expected to contain a single JSON object whose keys match the dataclass field names:
    ``title``, ``writer``, and ``release_year``. The loaded mapping is unpacked into the dataclass
    constructor so each JSON key is bound to the parameter with the same name.

    Validation is intentionally minimal in this example. The function assumes the JSON has the
    expected shape and relies on :func:`json.load` together with the dataclass constructor to fail
    if the structure is incompatible.

    :param file_path: Path to the JSON file to read.
    :type file_path: str | Path
    :returns: Parsed comic instance built from the JSON object.
    :rtype: Comic
    """

    with Path(file_path).open("r", encoding="utf-8") as file:
        data = json.load(file)
        return Comic(**data)
