import numpy as np
import pandas as pd

from my_python_project.pandas_vectorization_demo import (
    make_transactions_dataframe,
    process_with_iterrows,
    process_with_vectorization,
)


def test_make_transactions_dataframe_structure() -> None:
    df = make_transactions_dataframe(row_count=10)

    assert len(df) == 10
    assert list(df.columns) == ["timestamp", "amount", "currency"]
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    assert pd.api.types.is_float_dtype(df["amount"])


def test_process_with_vectorization_adds_expected_columns() -> None:
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2024-01-01 23:30:00", "2024-01-01 10:15:00"]),
            "amount": [100.0, 50.0],
            "currency": ["EUR", "USD"],
        }
    )

    result = process_with_vectorization(df)

    expected_columns = {
        "timestamp",
        "amount",
        "currency",
        "hour",
        "is_night",
        "amount_zscore",
        "log_amount",
    }

    assert expected_columns.issubset(result.columns)
    assert result.loc[0, "hour"] == 23
    assert result.loc[1, "hour"] == 10
    assert result.loc[0, "is_night"]
    assert not result.loc[1, "is_night"]


def test_iterrows_and_vectorized_match_on_small_dataframe() -> None:
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(
                [
                    "2024-01-01 23:30:00",
                    "2024-01-01 05:00:00",
                    "2024-01-01 12:15:00",
                ]
            ),
            "amount": [100.0, 250.0, 50.0],
            "currency": ["EUR", "USD", "GBP"],
        }
    )

    slow_result = process_with_iterrows(df)
    fast_result = process_with_vectorization(df)

    assert np.array_equal(
        slow_result["hour"].to_numpy(),
        fast_result["hour"].to_numpy(),
    )
    assert slow_result["is_night"].equals(fast_result["is_night"])
    assert np.allclose(
        slow_result["amount_zscore"].to_numpy(),
        fast_result["amount_zscore"].to_numpy(),
    )
    assert np.allclose(
        slow_result["log_amount"].to_numpy(),
        fast_result["log_amount"].to_numpy(),
    )


def test_log_amount_handles_zero_correctly() -> None:
    df = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(["2024-01-01 08:00:00"]),
            "amount": [0.0],
            "currency": ["EUR"],
        }
    )

    result = process_with_vectorization(df)

    assert result.loc[0, "log_amount"] == 0.0
