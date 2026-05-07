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
replaced with `_`. This is used in dbt project configuration and profile naming.

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

**type_checker**

`"ty"` or `"mypy"`. Controls which Python type checker is added to the generated project and used by `task check` and CI.

---
