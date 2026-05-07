<p align="center">
  <img width="600" src="static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
</style>

---

This is a Cookiecutter template for private corporate dbt repositories using DBT Fusion. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://docs.astral.sh/ruff/), [mypy](https://mypy.readthedocs.io/en/stable/)/[ty](https://docs.astral.sh/ty/)
- Python testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- DBT Fusion CI with a baked `selectors.yml` and DuckDB CI profile

An example of a repository generated with this package can be found [here](https://github.com/VDFaller/cookiecutter-dbt-example).

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/VDFaller/cookiecutter-dbt.git
```

or if you don't have `uv` installed yet:

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

### Acknowledgements

This project is a fork and adaptation of
[osprey-oss/cookiecutter-uv](https://github.com/osprey-oss/cookiecutter-uv),
which itself traces back to
[Audrey Feldroy's cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
