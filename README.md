<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/VDFaller/cookiecutter-dbt/main/docs/static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/VDFaller/cookiecutter-dbt/main.yml?branch=main)](https://github.com/VDFaller/cookiecutter-dbt/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/VDFaller/cookiecutter-dbt/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://VDFaller.github.io/cookiecutter-dbt/)
[![License](https://img.shields.io/github/license/VDFaller/cookiecutter-dbt)](https://img.shields.io/github/license/VDFaller/cookiecutter-dbt)

This is a Cookiecutter template for private corporate dbt repositories using DBT Fusion. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://docs.astral.sh/ruff/) and optional [ty](https://docs.astral.sh/ty/)/[mypy](https://mypy.readthedocs.io/en/stable/)
- Python testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- DBT Fusion CI with a baked `selectors.yml` and DuckDB CI profile

---

<p align="center">
  <a href="https://VDFaller.github.io/cookiecutter-dbt/">Documentation</a> - <a href="https://github.com/VDFaller/cookiecutter-dbt-example">Example</a>
</p>

---

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/VDFaller/cookiecutter-dbt.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/VDFaller/cookiecutter-dbt.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

## Acknowledgements

This project is a fork and adaptation of
[osprey-oss/cookiecutter-uv](https://github.com/osprey-oss/cookiecutter-uv),
which itself traces back to
[Audrey Feldroy's cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
