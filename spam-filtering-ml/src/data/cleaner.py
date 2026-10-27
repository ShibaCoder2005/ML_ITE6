"""Xử lý giá trị trống, loại bỏ ký tự lạ và lọc từ dừng."""

from __future__ import annotations

import re
import string
from typing import Iterable, Optional

import pandas as pd

# Stop-words tiếng Anh tối giản (mở rộng bằng NLTK khi cần)
DEFAULT_STOPWORDS = frozenset(
    {
        "a", "an", "the", "and", "or", "but", "if", "in", "on", "at", "to",
        "for", "of", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "must", "shall", "can", "this", "that",
        "these", "those", "i", "you", "he", "she", "it", "we", "they",
        "me", "him", "her", "us", "them", "my", "your", "his", "its",
        "our", "their", "what", "which", "who", "whom", "with", "from",
        "by", "as", "not", "no", "nor", "so", "than", "too", "very",
    }
)


def clean_text(
    text: str,
    *,
    lowercase: bool = True,
    remove_punctuation: bool = True,
    remove_digits: bool = False,
    stopwords: Optional[Iterable[str]] = DEFAULT_STOPWORDS,
) -> str:
    """Làm sạch một chuỗi văn bản: chuẩn hóa chữ thường, lọc nhiễu, stop-words."""
    if not isinstance(text, str) or not text.strip():
        return ""

    out = text.strip()
    if lowercase:
        out = out.lower()

    # URL / email thô
    out = re.sub(r"https?://\S+|www\.\S+", " ", out)
    out = re.sub(r"\S+@\S+", " ", out)

    if remove_punctuation:
        out = out.translate(str.maketrans("", "", string.punctuation))
    if remove_digits:
        out = re.sub(r"\d+", " ", out)

    out = re.sub(r"\s+", " ", out).strip()

    if stopwords is not None:
        sw = set(stopwords)
        tokens = [t for t in out.split() if t not in sw]
        out = " ".join(tokens)

    return out


def clean_dataframe(
    df: pd.DataFrame,
    *,
    text_col: str = "text",
    drop_empty: bool = True,
    **clean_kwargs,
) -> pd.DataFrame:
    """Áp dụng ``clean_text`` lên cột văn bản; tùy chọn loại bỏ dòng trống sau làm sạch."""
    result = df.copy()
    result[text_col] = result[text_col].fillna("").astype(str).map(
        lambda t: clean_text(t, **clean_kwargs)
    )
    if drop_empty:
        result = result[result[text_col].str.len() > 0].reset_index(drop=True)
    return result
