import importlib.util
import pathlib


MODULE_DIR = pathlib.Path(__file__).resolve().parents[1]
EXERCISES_PATH = MODULE_DIR / "exercises.py"

spec = importlib.util.spec_from_file_location("basics_exercises", EXERCISES_PATH)
ex = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(ex)


def test_add_two_numbers():
    assert ex.add_two_numbers(2, 3) == 5
    assert ex.add_two_numbers(-1, 1) == 0


def test_repeat_text():
    assert ex.repeat_text("a", 3) == "aaa"
    assert ex.repeat_text("hi", 0) == ""


def test_is_even():
    assert ex.is_even(2) is True
    assert ex.is_even(3) is False
    assert ex.is_even(0) is True

