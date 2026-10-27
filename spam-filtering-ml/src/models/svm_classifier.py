"""SVM tìm siêu phẳng tối ưu lề cực đại (LinearSVC / SVC soft-margin)."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal, Optional

import joblib
from sklearn.svm import LinearSVC, SVC


def train_svm(
    X_train,
    y_train,
    *,
    C: float = 1.0,
    kernel: Literal["linear", "rbf", "poly", "sigmoid"] = "linear",
    use_linear_svc: bool = True,
    class_weight: Optional[str] = "balanced",
    random_state: int = 42,
    max_iter: int = 5000,
):
    """
    Huấn luyện SVM lề mềm.

    Với ma trận TF-IDF thưa, mặc định dùng ``LinearSVC`` (hiệu quả hơn SVC kernel linear).
    Đặt ``use_linear_svc=False`` để khảo sát kernel RBF/poly/sigmoid.
    """
    if use_linear_svc and kernel == "linear":
        model = LinearSVC(
            C=C,
            class_weight=class_weight,
            random_state=random_state,
            max_iter=max_iter,
            dual="auto",
        )
    else:
        model = SVC(
            C=C,
            kernel=kernel,
            class_weight=class_weight,
            random_state=random_state,
            probability=False,
        )
    model.fit(X_train, y_train)
    return model


def save_model(model: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str | Path):
    return joblib.load(path)
