# Tutorial

This page contains a complete tutorial on how to create your project.

## Step 1: Install uv

To start, we will need to install `uv`. The instructions to install uv can be found
[here](https://docs.astral.sh/uv/#getting-started). For MacOS or Linux;

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Step 2: Generate your project

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/VDFaller/cookiecutter-dbt.git
```

For an explanation of the prompt arguments, see
[Prompt Arguments](prompt_arguments.md).

## Step 3: Set up your Github repository

Create an empty [new repository](https://github.com/new) on Github. Give
it a name that only contains alphanumeric characters and optionally `-`.
DO NOT check any boxes under the option `Initialize this repository
with`.

## Step 4: Upload your project to Github

Run the following commands, replacing `<project-name>` with the name
that you also gave the Github repository and `<github_author_handle>`
with your Github username.

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

### Step 5: Set Up Your Development Environment

Initially, the CI/CD pipeline will fail for two reasons:

- The project does not yet contain a `uv.lock` file
- There are a few formatting issues in the project

To fix that, we first install the environment and the pre-commit hooks with:

```bash
task install
```

This will generate the `uv.lock` file

### Step 6: Run the pre-commit hooks

Now, to resolve the formatting issues, let's run the pre-commit hooks:

```bash
uv run pre-commit run -a
```

### 7. Commit the changes

Now we commit the changes made by the two steps above to the repository:

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

## Step 8: You're all set!

That's it! I hope this repository saved you a lot of manual configuration. If you have any improvement suggestions, feel
free to raise an issue or open a PR on Github!
