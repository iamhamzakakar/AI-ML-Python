from __future__ import annotations

import time
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class BenchmarkResult:
    method_name: str
    elapsed_seconds: float


def make_transactions_dataframe(row_count: int = 1_000_000) -> pd.DataFrame:
    """Create a synthetic transaction DataFrame for benchmarking.

    Args:
        row_count: Number of rows to generate.

    Returns:
        A DataFrame containing timestamps, amounts, and currencies.
    """
    rng = np.random.default_rng(seed=42)

    start_timestamp = pd.Timestamp("2024-01-01 00:00:00")
    random_minutes = rng.integers(0, 60 * 24 * 30, size=row_count)
    timestamps = start_timestamp + pd.to_timedelta(random_minutes, unit="m")

    amounts = rng.gamma(shape=2.0, scale=120.0, size=row_count)
    currencies = rng.choice(["EUR", "USD", "GBP", "SEK"], size=row_count)

    return pd.DataFrame(
        {
            "timestamp": timestamps,
            "amount": amounts,
            "currency": currencies,
        }
    )


def process_with_iterrows(df: pd.DataFrame) -> pd.DataFrame:
    """Process transaction data using a slow row-by-row loop.

    Args:
        df: Input transaction DataFrame.

    Returns:
        A new DataFrame with engineered features added.
    """
    result_df = df.copy()

    mean_amount = result_df["amount"].mean()
    std_amount = result_df["amount"].std()

    hours: list[int] = []
    is_night_flags: list[bool] = []
    amount_zscores: list[float] = []
    log_amounts: list[float] = []

    for _, row in result_df.iterrows():
        timestamp = row["timestamp"]
        amount = float(row["amount"])

        hour = int(timestamp.hour)
        is_night = hour >= 22 or hour <= 6
        amount_zscore = (amount - mean_amount) / std_amount
        log_amount = float(np.log1p(max(amount, 0.0)))

        hours.append(hour)
        is_night_flags.append(is_night)
        amount_zscores.append(amount_zscore)
        log_amounts.append(log_amount)

    result_df["hour"] = hours
    result_df["is_night"] = is_night_flags
    result_df["amount_zscore"] = amount_zscores
    result_df["log_amount"] = log_amounts
    result_df["currency"] = result_df["currency"].astype("category")

    return result_df


def process_with_vectorization(df: pd.DataFrame) -> pd.DataFrame:
    """Process transaction data using vectorized pandas operations.

    Args:
        df: Input transaction DataFrame.

    Returns:
        A new DataFrame with engineered features added.
    """
    result_df = df.copy()

    result_df["hour"] = result_df["timestamp"].dt.hour
    result_df["is_night"] = (result_df["hour"] >= 22) | (result_df["hour"] <= 6)
    result_df["amount_zscore"] = (
        result_df["amount"] - result_df["amount"].mean()
    ) / result_df["amount"].std()
    result_df["log_amount"] = np.log1p(result_df["amount"].clip(lower=0))
    result_df["currency"] = result_df["currency"].astype("category")

    return result_df


def benchmark_pipeline() -> None:
    """Benchmark iterrows and vectorized pandas pipelines."""
    df = make_transactions_dataframe(row_count=1_000_000)

    print(f"Created DataFrame with {len(df):,} rows")

    start_iterrows = time.perf_counter()
    iterrows_df = process_with_iterrows(df)
    iterrows_time = time.perf_counter() - start_iterrows

    start_vectorized = time.perf_counter()
    vectorized_df = process_with_vectorization(df)
    vectorized_time = time.perf_counter() - start_vectorized

    speedup = iterrows_time / vectorized_time

    print(f"Iterrows time:    {iterrows_time:.4f} seconds")
    print(f"Vectorized time:  {vectorized_time:.4f} seconds")
    print(f"Speedup:          {speedup:.2f}x")

    print("\nSample output from vectorized pipeline:")
    print(vectorized_df.head())

    print("\nColumn equality check:")
    print(
        "hour:",
        np.array_equal(
            iterrows_df["hour"].to_numpy(),
            vectorized_df["hour"].to_numpy(),
        ),
    )
    print("is_night:", iterrows_df["is_night"].equals(vectorized_df["is_night"]))
    print(
        "amount_zscore:",
        np.allclose(iterrows_df["amount_zscore"], vectorized_df["amount_zscore"]),
    )
    print(
        "log_amount:",
        np.allclose(iterrows_df["log_amount"], vectorized_df["log_amount"]),
    )


if __name__ == "__main__":
    benchmark_pipeline()
