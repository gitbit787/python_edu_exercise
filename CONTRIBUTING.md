# Contributing to the Python Education Repository

Thank you for your interest in improving this educational project!

This repository is organized into **beginner**, **intermediate**, **advanced**, **projects**, and **exercises** sections. The guidelines below explain how to add or modify content while keeping everything consistent and easy to navigate.

## General guidelines

- Follow **PEP 8** style. Use clear, descriptive names.
- Prefer **type hints** in intermediate and advanced code.
- Keep examples **small and focused**. Longer work should go in `projects/`.
- Write **docstrings** for public functions, especially in exercises and solutions.
- When in doubt, look at existing folders (e.g. `beginner/01_basics`) and copy the structure.

## Folder naming conventions

- Beginner topics live in `beginner/` and are numbered:
  - `beginner/01_basics/`
  - `beginner/02_variables_and_types/`
- Future beginner topics should continue this pattern:
  - `beginner/03_control_flow/`
  - `beginner/04_loops/`
  - etc.
- Intermediate and advanced topics should use descriptive folder names without numbers (for now), e.g.:
  - `intermediate/data_structures_deeper/`
  - `advanced/decorators/`

## Adding a new lesson (topic)

To add a new topic at any level:

1. **Create a new folder** under the appropriate level, for example:
   - `beginner/03_control_flow/`
   - `intermediate/error_handling/`
   - `advanced/typing/`
2. Inside that folder, add:
   - `README.md` – concept overview and how to use the files.
   - `lesson.py` – runnable examples demonstrating the concept.
   - `exercises.py` – functions with docstrings and clear TODO-style comments.
   - `solutions.py` – reference implementations that match the exercises.
   - `tests/` (optional but recommended) – `test_*.py` files using `pytest`.
3. If you add tests:
   - Follow the pattern in `beginner/01_basics/tests/` and `beginner/02_variables_and_types/tests/`.
   - Keep tests small and focused on behavior, not implementation details.

## Adding or updating exercises

- Place new exercises in the relevant level/topic folder’s `exercises.py`.
- Each exercise should:
  - Have a clear **docstring** explaining the task.
  - Avoid printing unless the goal is to practice I/O.
  - Be testable with pure Python functions when possible.
- If you add a substantial exercise:
  - Add or update tests in `tests/test_*.py`.

## Adding a project

Projects live under `projects/` and are grouped by level:

- `projects/beginner/`
- `projects/intermediate/`
- `projects/advanced/`

For each new project, create a folder like:

- `projects/beginner/number_guessing_game/`

Inside it, include:

- `README.md` – project description, learning goals, and how to run it.
- `starter/` – starter code skeleton (optional).
- `solution/` – reference implementation.
- `tests/` – automated tests if applicable.

## Documentation updates

If you add new major topics or projects:

- Update `docs/curriculum_map.md` to include them in the appropriate path.
- Optionally, add notes for instructors in a future `docs/teaching_guide.md`.

## Tests and tooling

- Before opening a pull request, run:
  - `python -m venv .venv` (once)
  - Activate the environment
  - `pip install -r requirements.txt`
  - `pytest`
- Contributions that add code should include tests when reasonable.

## Issue and PR templates

This repository may include templates under `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`. When present:

- Use the **lesson request** issue template to propose new topics.
- Use the PR template checklist to ensure:
  - Tests pass.
  - Docs are updated.
  - Naming and structure follow existing patterns.

Thank you for helping make this Python education resource better for everyone!

