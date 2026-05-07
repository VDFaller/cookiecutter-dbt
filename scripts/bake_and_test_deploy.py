from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "cookiecutter-dbt-example"


def run(*args: str, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(  # noqa: S603 - arguments are fixed by this script, not user-supplied
        args,
        cwd=cwd or ROOT,
        check=check,
        text=True,
    )


def main() -> None:
    if PROJECT_DIR.exists():
        shutil.rmtree(PROJECT_DIR)

    run(
        "uv",
        "run",
        "cookiecutter",
        "--no-input",
        ".",
        "--overwrite-if-exists",
        "author=Vince Faller",
        "email=vdfaller@gmail.com",
        "github_author_handle=VDFaller",
        "project_name=cookiecutter-dbt-example",
        "project_slug=cookiecutter_dbt_example",
    )

    run("uv", "sync", cwd=PROJECT_DIR)
    run("git", "init", "-b", "main", cwd=PROJECT_DIR)
    run("git", "add", ".", cwd=PROJECT_DIR)
    run("uv", "run", "pre-commit", "install", cwd=PROJECT_DIR)

    # Mirror the Makefile behavior by allowing pre-commit failures here.
    run("uv", "run", "pre-commit", "run", "-a", cwd=PROJECT_DIR, check=False)
    run("git", "add", ".", cwd=PROJECT_DIR)
    run("uv", "run", "pre-commit", "run", "-a", cwd=PROJECT_DIR, check=False)
    run("git", "add", ".", cwd=PROJECT_DIR)

    run("git", "commit", "-m", "init commit", cwd=PROJECT_DIR)
    run(
        "git",
        "remote",
        "add",
        "origin",
        "git@github.com:VDFaller/cookiecutter-dbt-example.git",
        cwd=PROJECT_DIR,
    )
    run("git", "push", "-f", "origin", "main", cwd=PROJECT_DIR)


if __name__ == "__main__":
    main()
