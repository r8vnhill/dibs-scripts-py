# AI Agent Guide

Context and essential rules for agents working in this subproject.

## Decision Protocol

- Never make product, architecture, pedagogy, content-order, or style-policy decisions on your own.
- When a choice is required, present viable alternatives with their tradeoffs and wait for confirmation from the user.
- You may proceed with low-risk mechanical changes only when the existing repository pattern makes the decision unambiguous.
- If an instruction conflicts with project patterns, stop and ask before changing direction.

## Project Shape

- This is the Python companion repository for DIBS scripting lessons.
- It targets Python 3.14+ and uses `uv` for environment and command execution.
- `readme_gen/` is a package-style CLI example with validation, parser setup, logging, and an entry point.
- `structured-output/` is a script-first example using sibling imports, JSON persistence, and a `Comic` dataclass model.

## Workflow

- Sync the environment with `uv sync`.
- Run the README generator with `uv run -m readme_gen.new_readme --help` or `uv run -m readme_gen.new_readme --name "Utility Scripts - DIBS" --out_dir .`.
- For `structured-output/`, keep the script-first layout in mind and run commands from that directory when sibling imports require it.
- There is no verified test command in the current project files; do not invent one without adding the required test setup.

## Code Conventions

- Keep lesson code clear and explicit rather than over-engineered.
- Preserve `argparse`-based CLI contracts in `readme_gen/`.
- Use `pathlib.Path` for filesystem paths and keep validation behavior explicit.
- Use dataclasses when the lesson needs a stable model; use dictionaries where the lesson is about flexible JSON-shaped data.
- Keep repository docs in English while preserving Spanish course references and names.
- Follow the inclusive documentation guidance from `../astro-website/src/pages/notes/software-libraries/api-design/documentation/index.astro`: prefer precise, clear, respectful terminology over loaded metaphors or unnecessarily punitive wording.
- Avoid terms such as `violation` or `violations` in new CLI messages, docs, test names, public fields, and API names when a more descriptive alternative works. Prefer `finding`, `issue`, `not allowed`, `policy mismatch`, or a domain-specific name.
- Do not rename existing CLI flags, dataclass fields, or documented outputs mechanically. If compatibility is involved, propose aliases, deprecation, release notes, or a migration path first.
