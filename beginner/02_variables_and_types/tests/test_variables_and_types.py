import importlib.util
import pathlib

import pytest


MODULE_DIR = pathlib.Path(__file__).resolve().parents[1]
EXERCISES_PATH = MODULE_DIR / "exercises.py"

spec = importlib.util.spec_from_file_location("variables_and_types_exercises", EXERCISES_PATH)
ex = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(ex)


def test_format_greeting():
    result = ex.format_greeting("Alice", 30)
    assert "Alice" in result
    assert "30" in result


def test_calculate_bmi():
    bmi = ex.calculate_bmi(70.0, 1.75)
    assert pytest.approx(bmi, rel=1e-3) == 22.86


def test_to_boolean():
    assert ex.to_boolean("true") is True
    assert ex.to_boolean("YES") is True
    assert ex.to_boolean("1") is True
    assert ex.to_boolean("false") is False
    assert ex.to_boolean("No") is False
    assert ex.to_boolean("0") is False

