import pytest

from my_python_project.refactored_functions import (
    calculate_average,
    clean_names,
    count_words,
    filter_passing_scores,
    find_high_risk_amounts,
)


def test_clean_names() -> None:
    result = clean_names(["  Alice  ", "BOB", " Charlie "])
    assert result == ["alice", "bob", "charlie"]


def test_filter_passing_scores() -> None:
    result = filter_passing_scores([45.0, 67.5, 80.0, 39.0], 50.0)
    assert result == [67.5, 80.0]


def test_calculate_average() -> None:
    result = calculate_average([10.0, 20.0, 30.0])
    assert result == 20.0


def test_calculate_average_raises_for_empty_list() -> None:
    with pytest.raises(ValueError, match="values must not be empty"):
        calculate_average([])


def test_find_high_risk_amounts() -> None:
    result = find_high_risk_amounts(
        risk_scores=[0.2, 0.9, 0.75, 0.4],
        amounts=[100.0, 250.0, 80.0, 50.0],
        threshold=0.7,
    )
    assert result == [250.0, 80.0]


def test_find_high_risk_amounts_raises_for_mismatched_lengths() -> None:
    with pytest.raises(
        ValueError, match="risk_scores and amounts must have the same length"
    ):
        find_high_risk_amounts(
            risk_scores=[0.2, 0.9],
            amounts=[100.0],
            threshold=0.7,
        )


def test_count_words() -> None:
    result = count_words("Python is fun to learn")
    assert result == 5
