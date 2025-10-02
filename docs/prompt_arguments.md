# Prompt arguments

When running the command `ccp` a prompt will start which enables you to configure your repository. The
prompt values and their explanation are as follows:

---

**author**

Your full name.

**email**

Your email address.

**author_github_handle**

Your github handle, i.e. `<handle>` in `https://github.com/<handle>`

**project_name**

Your project name. Should be equal to the name of your repository
and it should only contain alphanumeric characters and `-`'s.

**project_slug**

The project slug, will default to the `project_name` with all `-`'s
replaced with `_`. This will be how you import your code later, e.g.

```python
from <project_slug> import foo
```

**project_description**

A short description of your project.

**project_type**
`"single project"` or `"dbt mesh"`. 
Choose `"single project"` if you want to create a single dbt core or fusion project. 
Choose `"dbt mesh"` if you want to create a repository that can contain multiple dbt core or fusion projects. 
[Intro to DBT Mesh](https://docs.getdbt.com/best-practices/how-we-mesh/mesh-1-intro)

**include_github_actions**

`"y"` or `"n"`. Adds a `.github` directory with various actions and
workflows to setup the environment and run code formatting checks
and unittests.

**publish_to_pypi**

`"y"` or `"n"`. Adds functionality to the
`Makefile` and Github workflows to make publishing your code as
simple as creating a new release release on Github. For more info,
see
[Publishing to PyPI](./features/publishing.md).


**codecov**

`"y"` or `"n"`. Adds code coverage checks with [codecov](https://about.codecov.io/).

**dockerfile**

`"y"` or `"n"`. Adds a simple [Dockerfile](https://docker.com).

**devcontainer**

`"y"` or `"n"`. Adds a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) specification to the project along with pre-installed pre-commit hooks and VSCode python extension configuration.

**open_source_license**

Choose a [license](https://choosealicense.com/). Options:
`["1. MIT License", "2. BSD license", "3. ISC license",  "4. Apache Software License 2.0", "5. GNU General Public License v3", "6. Not open source"]`

---
