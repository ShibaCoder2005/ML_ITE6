"""Multinomial Naive Bayes với Laplace smoothing xử lý từ vựng mới."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import joblib
from sklearn.naive_bayes import MultinomialNB


def train_multinomial_nb(
    X_train,
    y_train,
    *,
    alpha: float = 1.0,
    fit_prior: bool = True,
) -> MultinomialNB:
    """
    Huấn luyện MultinomialNB.

    Parameters
    ----------
    alpha : float
        Hệ số Laplace / Lidstone smoothing (mặc định 1.0).
    """
    model = MultinomialNB(alpha=alpha, fit_prior=fit_prior)
    model.fit(X_train, y_train)
    return model


def save_model(model: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str | Path) -> MultinomialNB:
    return joblib.load(path)
