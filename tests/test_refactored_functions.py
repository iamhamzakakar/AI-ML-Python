from my_python_project.refactored_functions import filter_high_values


def test_filter_high_values() -> None:
    result = filter_high_values([1.0, 5.0, 8.0], 4.0)
    assert result == [5.0, 8.0]
