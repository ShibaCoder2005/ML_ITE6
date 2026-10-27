"""Thuật toán phân tách phân tầng bảo toàn tỷ lệ nhãn (Stratified Split)."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def stratified_train_val_test_split(
    df: pd.DataFrame,
    *,
    label_col: str = "label",
    train_size: float = 0.6,
    val_size: float = 0.2,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Chia Train / Val / Test theo tỷ lệ mặc định 60 / 20 / 20, giữ tỷ lệ nhãn.
    """
    total = train_size + val_size + test_size
    if abs(total - 1.0) > 1e-6:
        raise ValueError(f"Tổng tỷ lệ phải = 1.0, nhận được {total}")

    train_df, temp_df = train_test_split(
        df,
        test_size=(val_size + test_size),
        stratify=df[label_col],
        random_state=random_state,
    )
    relative_test = test_size / (val_size + test_size)
    val_df, test_df = train_test_split(
        temp_df,
        test_size=relative_test,
        stratify=temp_df[label_col],
        random_state=random_state,
    )
    return (
        train_df.reset_index(drop=True),
        val_df.reset_index(drop=True),
        test_df.reset_index(drop=True),
    )


def save_splits(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    output_dir: str | Path,
) -> None:
    """Ghi ``train.csv``, ``val.csv``, ``test.csv`` vào thư mục splits."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(output_dir / "train.csv", index=False)
    val_df.to_csv(output_dir / "val.csv", index=False)
    test_df.to_csv(output_dir / "test.csv", index=False)
