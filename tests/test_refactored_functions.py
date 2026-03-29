import pytest

from my_python_project.refactored_functions import (
    calculate_average,
    clean_names,
    filter_passing_scores,
)


@pytest.mark.parametrize(
    ("names", "expected"),
    [
        (["  Alice  ", "BOB", " Charlie "], ["alice", "bob", "charlie"]),  # happy path
        ([], []),  # edge case
    ],
)
def test_clean_names(names: list[str], expected: list[str]) -> None:
    assert clean_names(names) == expected


@pytest.mark.parametrize(
    ("scores", "pass_mark", "expected"),
    [
        ([45.0, 67.5, 80.0, 39.0], 50.0, [67.5, 80.0]),  # happy path
        ([50.0, 49.9, 50.1], 50.0, [50.0, 50.1]),  # edge case: boundary values
    ],
)
def test_filter_passing_scores(
    scores: list[float], pass_mark: float, expected: list[float]
) -> None:
    assert filter_passing_scores(scores, pass_mark) == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([10.0, 20.0, 30.0], 20.0),  # happy path
        ([5.0], 5.0),  # edge case: single value
    ],
)
def test_calculate_average(values: list[float], expected: float) -> None:
    assert calculate_average(values) == expected


def test_calculate_average_raises_for_empty_list() -> None:
    with pytest.raises(ValueError, match="values must not be empty"):
        calculate_average([])
