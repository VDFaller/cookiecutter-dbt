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
        └── main.yml

`main.yml` runs three jobs:

- `quality` for formatting and lint checks
- `tests-and-type-check` across the configured Python matrix
- `dbtf-tests` for pull request dbt validation using DBT Fusion

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

Additionally, the Python test job checks compatibility with multiple Python
versions.
