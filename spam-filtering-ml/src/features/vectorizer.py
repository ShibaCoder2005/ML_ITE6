"""Xây dựng ma trận TF-IDF trong không gian vector n-chiều."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional, Tuple

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf_vectorizer(
    *,
    max_features: Optional[int] = 5000,
    ngram_range: Tuple[int, int] = (1, 2),
    min_df: int = 2,
    max_df: float = 0.95,
    sublinear_tf: bool = True,
) -> TfidfVectorizer:
    """Khởi tạo ``TfidfVectorizer`` với cấu hình mặc định phù hợp SMS/email."""
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        sublinear_tf=sublinear_tf,
    )


def fit_transform_tfidf(
    texts: Iterable[str],
    vectorizer: Optional[TfidfVectorizer] = None,
    **kwargs,
):
    """Fit trên tập Train và trả về (vectorizer, X)."""
    vec = vectorizer or build_tfidf_vectorizer(**kwargs)
    X = vec.fit_transform(texts)
    return vec, X


def transform_tfidf(vectorizer: TfidfVectorizer, texts: Iterable[str]):
    """Biến đổi văn bản bằng vectorizer đã fit."""
    return vectorizer.transform(texts)


def save_vectorizer(vectorizer: TfidfVectorizer, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, path)


def load_vectorizer(path: str | Path) -> TfidfVectorizer:
    return joblib.load(path)
