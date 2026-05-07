# CI/CD with GitHub Actions

When `include_github_actions` is set to `"y"`, the generated project includes a
single `.github/workflows/main.yml` workflow plus two local setup actions:

    .github
    ├── actions
    │   ├── setup-dbtf-env
    │   │   └── action.yml
    │   └── setup-python-env
    │       └── action.yml
    ├── profiles.yml
    └── workflows
        ├── main.yml
        └── on-release-main.yml

`main.yml` runs three jobs:

- `quality` for formatting and lint checks
- `tests-and-type-check` across the configured Python matrix
- `dbtf-tests` for pull request and `main` branch dbt validation using DBT Fusion

The DBT Fusion job stays DuckDB-based and uses the baked CI profile in
`.github/profiles.yml`. For pull requests, it fetches enough Git history to
compute the merge base against `origin/main`, parses the project at that merge
base, saves `target/manifest.json` as state, restores the PR head, and runs:

```bash
dbtf build --selector ci_run --state .github/dbtf-state --profiles-dir .github -t ci --defer
```

The generated repository also includes a baked `selectors.yml` with a generic
`ci_run` selector. That selector supports two CI patterns out of the box:

- Put singular tests that should always run in PR CI under `tests/ci_tests/`
- Use state selection to run modified nodes, their immediate children, and
  bridge nodes between upstream and downstream modified changes

If `mkdocs` is set to `"y"`, `on-release-main.yml` deploys the documentation
site whenever a new release is made on GitHub.

Additionally, the Python test job checks compatibility with multiple Python
versions.

## How to trigger a release?

To trigger a new release, navigate to your repository on GitHub, click `Releases` on the right, and then select `Draft
a new release`. If you fail to find the button, you could also directly visit
`https://github.com/<username>/<repository-name>/releases/new`.

Give your release a title, and add a new tag in the form `*.*.*` where the
`*`'s are alphanumeric. To finish, press `Publish release`.
