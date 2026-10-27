"""Đọc và xác thực tính toàn vẹn của tập dữ liệu thô."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

REQUIRED_COLUMNS = ("text", "label")


def load_raw_dataset(
    path: str | Path,
    *,
    text_col: str = "text",
    label_col: str = "label",
    encoding: str = "utf-8",
) -> pd.DataFrame:
    """
    Đọc CSV dữ liệu thô và chuẩn hóa tên cột về ``text`` / ``label``.

    Raises
    ------
    FileNotFoundError
        Nếu đường dẫn không tồn tại.
    ValueError
        Nếu thiếu cột bắt buộc hoặc dữ liệu rỗng.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy file dữ liệu: {path}")

    df = pd.read_csv(path, encoding=encoding)
    rename_map = {}
    if text_col != "text" and text_col in df.columns:
        rename_map[text_col] = "text"
    if label_col != "label" and label_col in df.columns:
        rename_map[label_col] = "label"
    if rename_map:
        df = df.rename(columns=rename_map)

    _validate_dataframe(df, REQUIRED_COLUMNS)
    return df[["text", "label"]].copy()


def _validate_dataframe(df: pd.DataFrame, required: Iterable[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu cột bắt buộc: {missing}. Có: {list(df.columns)}")
    if df.empty:
        raise ValueError("Tập dữ liệu rỗng.")
    if df["text"].isna().all():
        raise ValueError("Cột text toàn giá trị trống.")
