from pathlib import Path


def test_selectors_file_exists() -> None:
    assert Path("selectors.yml").exists()
