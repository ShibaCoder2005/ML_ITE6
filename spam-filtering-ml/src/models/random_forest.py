"""Random Forest ensemble dựa trên bootstrapping và tập con thuộc tính."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import joblib
from sklearn.ensemble import RandomForestClassifier


def train_random_forest(
    X_train,
    y_train,
    *,
    n_estimators: int = 200,
    max_depth: Optional[int] = None,
    min_samples_split: int = 2,
    class_weight: Optional[str] = "balanced",
    random_state: int = 42,
    n_jobs: int = -1,
) -> RandomForestClassifier:
    """Huấn luyện Random Forest làm mô hình đối chứng (No Free Lunch)."""
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        class_weight=class_weight,
        random_state=random_state,
        n_jobs=n_jobs,
    )
    model.fit(X_train, y_train)
    return model


def save_model(model: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str | Path) -> RandomForestClassifier:
    return joblib.load(path)
