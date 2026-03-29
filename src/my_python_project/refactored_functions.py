from collections.abc import Sequence


def clean_names(names: Sequence[str]) -> list[str]:
    """Clean names by removing extra spaces and converting to lowercase.

    Args:
        names: A sequence of name strings.

    Returns:
        A list of cleaned name strings.
    """
    return [name.strip().lower() for name in names]


def filter_passing_scores(scores: Sequence[float], pass_mark: float) -> list[float]:
    """Return scores that are greater than or equal to the pass mark.

    Args:
        scores: A sequence of numeric scores.
        pass_mark: The minimum passing score.

    Returns:
        A list of scores that meet or exceed the pass mark.
    """
    return [score for score in scores if score >= pass_mark]


def calculate_average(values: Sequence[float]) -> float:
    """Calculate the average of numeric values.

    Args:
        values: A sequence of numeric values.

    Returns:
        The arithmetic mean of the values.

    Raises:
        ValueError: If the input sequence is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def find_high_risk_amounts(
    risk_scores: Sequence[float],
    amounts: Sequence[float],
    threshold: float,
) -> list[float]:
    """Return transaction amounts whose risk scores are above a threshold.

    Args:
        risk_scores: A sequence of risk scores.
        amounts: A sequence of transaction amounts.
        threshold: The risk threshold.

    Returns:
        A list of amounts whose corresponding risk score is above the threshold.

    Raises:
        ValueError: If the input sequences do not have the same length.
    """
    if len(risk_scores) != len(amounts):
        raise ValueError("risk_scores and amounts must have the same length")

    return [
        amount
        for risk_score, amount in zip(risk_scores, amounts)
        if risk_score > threshold
    ]


def count_words(text: str) -> int:
    """Count the number of words in a text string.

    Args:
        text: Input text.

    Returns:
        The number of words in the text.
    """
    return len(text.split())
