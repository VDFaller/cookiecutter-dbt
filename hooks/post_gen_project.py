#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(path):
        os.remove(path)


def remove_dir(filepath: str) -> None:
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.isdir(path):
        shutil.rmtree(path)


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    shutil.move(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
