from typing import Sequence


def filter_high_values(numbers: Sequence[float], threshold: float) -> list[float]:
    """Return numbers greater than the given threshold.

    Args:
        numbers: A sequence of numeric values.
        threshold: The cutoff value.

    Returns:
        A list containing only numbers greater than the threshold.
    """
    return [number for number in numbers if number > threshold]
