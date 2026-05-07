from __future__ import annotations

import shlex
import subprocess

from tests.utils import file_contains_text, is_valid_yaml, run_within_dir


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()
    assert is_valid_yaml(result.project_path / "selectors.yml")
    assert is_valid_yaml(result.project_path / ".pre-commit-config.yaml")
    assert file_contains_text(f"{result.project_path}/selectors.yml", "name: ci_run")
    assert file_contains_text(f"{result.project_path}/selectors.yml", "path:tests/ci_tests")
    assert file_contains_text(f"{result.project_path}/selectors.yml", "state:modified+1")
    assert file_contains_text(f"{result.project_path}/selectors.yml", "+state:modified")
    assert file_contains_text(f"{result.project_path}/selectors.yml", "state:modified+")
    assert file_contains_text(f"{result.project_path}/.pre-commit-config.yaml", "dbt-checkpoint/dbt-checkpoint")
    assert file_contains_text(f"{result.project_path}/.pre-commit-config.yaml", "check-model-has-tests-by-group")
    assert file_contains_text(f"{result.project_path}/.pre-commit-config.yaml", "unique_combination_of_columns")
    assert file_contains_text(f"{result.project_path}/.pre-commit-config.yaml", "expect_compound_columns_to_be_unique")
    assert file_contains_text(
        f"{result.project_path}/{'packages.yml'}",
        "metaplane/dbt_expectations",
    )
    assert file_contains_text(f"{result.project_path}/macros/clean_text.sql", "macro clean_text")


def test_using_pytest(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert is_valid_yaml(result.project_path / "selectors.yml")

        # Install the uv environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("task test")) == 0


def test_dbtf_ci_workflow(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()

        workflow_path = result.project_path / ".github" / "workflows" / "main.yml"
        assert result.exit_code == 0
        assert is_valid_yaml(workflow_path)
        assert file_contains_text(workflow_path, "fetch-depth: 0")
        assert file_contains_text(workflow_path, "git fetch --no-tags --prune origin main")
        assert file_contains_text(workflow_path, 'PR_HEAD="$(git rev-parse HEAD)"')
        assert file_contains_text(workflow_path, 'MERGE_BASE="$(git merge-base origin/main "$PR_HEAD")"')
        assert file_contains_text(workflow_path, 'rm -rf "$STATE_DIR"')
        assert file_contains_text(workflow_path, 'git checkout --force "$MERGE_BASE"')
        assert file_contains_text(workflow_path, "dbtf parse --profiles-dir .github -t ci")
        assert file_contains_text(workflow_path, 'cp target/manifest.json "$STATE_DIR/manifest.json"')
        assert file_contains_text(workflow_path, 'git checkout --force "$PR_HEAD"')
        assert file_contains_text(
            workflow_path,
            'dbtf build --selector ci_run --state "$STATE_DIR" --profiles-dir .github -t ci --defer',
        )
        assert file_contains_text(workflow_path, "target/run_results.json")
        assert file_contains_text(workflow_path, "target/manifest.json")
