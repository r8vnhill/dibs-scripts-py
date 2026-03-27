# DIBS Python Scripts — Course Companion

[![Python 3.14+](https://img.shields.io/badge/Python-3.14%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-runner%20%26%20env%20manager-111827)](https://docs.astral.sh/uv/)
[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](./LICENSE)

Companion code for **DIBS** (*Diseño e Implementación de Bibliotecas de Software*),
focused on the scripting lessons.

The course is taught in Spanish, but this repository is kept in English for
broader reach.

This repository will grow as new lessons are added.

## Table of Contents

- [DIBS Python Scripts — Course Companion](#dibs-python-scripts--course-companion)
  - [Table of Contents](#table-of-contents)
  - [Lessons](#lessons)
  - [Quickstart](#quickstart)
    - [Requirements](#requirements)
    - [Run the lesson code](#run-the-lesson-code)
  - [Repository Layout](#repository-layout)
  - [Contributing](#contributing)
  - [License](#license)

## Lessons

1) [First script and parameter validation in Python](https://dibs.ravenhill.cl/notes/software-libraries/scripting/first-script/py/)
   - Focus: `argparse`-based CLI contracts, explicit parameter validation, basic
     logging, and a clear entry point.
   - Code: `readme_gen/`
2) [Structured output in Python](https://dibs.ravenhill.cl/notes/software-libraries/scripting/structured-output/py/)
   - Focus: JSON as persisted interoperable output, `dict` as a flexible
     transient container, and `@dataclass` as an explicit stable model.
   - Code: `structured-output/`

## Quickstart

### Requirements

- Python 3.14+ (see `pyproject.toml`)
- [`uv`](https://docs.astral.sh/uv/) (recommended for running the examples)

### Run the lesson code

```bash
# Create/sync the virtual environment (no runtime deps yet, but keeps things consistent)
uv sync

# Show CLI help
uv run -m readme_gen.new_readme --help

# Generate a README in the current directory
uv run -m readme_gen.new_readme --name "Utility Scripts - DIBS" --verbose

# Generate a README in a target directory
uv run -m readme_gen.new_readme --name "Utility Scripts - DIBS" --out_dir .
```

Tip: using `-m` (module execution) ensures imports work correctly within the
`readme_gen` package.

For the `structured-output/` example, keep the script-first layout in mind:
the files use sibling imports, so the commands above switch into that directory
before importing `comics` and `json_utils`.

## Repository Layout

- `readme_gen/`: lesson module implementing a small README generator
  - `validated_directory.py`: reusable `argparse` validator (`str` → `Path`)
  - `parser.py`: CLI contract definition (`--name`, `--verbose`, `--out_dir`)
  - `app_logging.py`: minimal logging setup
  - `new_readme.py`: entry point wiring everything together
- `structured-output/`: script-first example showing JSON persistence and an
  explicit data model
  - `json_utils.py`: recursive `JSONValue` alias plus JSON writing helper
  - `comics.py`: `Comic` dataclass and JSON-to-model conversion
  - `comic.json`: sample payload used by the structured-output example

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

BSD 2-Clause. See [LICENSE](LICENSE).
