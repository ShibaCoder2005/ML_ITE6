"""Tính toán Confusion Matrix, Accuracy, Precision, Recall và F1-score."""

from __future__ import annotations

from typing import Any, Dict, Optional, Sequence

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def evaluate_classifier(
    model: Any,
    X,
    y_true,
    *,
    average: str = "binary",
    pos_label: Optional[Any] = None,
    labels: Optional[Sequence] = None,
) -> Dict[str, Any]:
    """Đánh giá mô hình và trả về dict metrics + confusion matrix."""
    y_pred = model.predict(X)

    kwargs = {"average": average}
    if pos_label is not None:
        kwargs["pos_label"] = pos_label

    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0, **kwargs)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0, **kwargs)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0, **kwargs)),
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=labels).tolist(),
        "y_pred": np.asarray(y_pred),
    }
    return metrics


def classification_report_dict(
    y_true,
    y_pred,
    *,
    target_names: Optional[Sequence[str]] = None,
) -> Dict[str, Any]:
    """Bọc ``classification_report(..., output_dict=True)``."""
    return classification_report(
        y_true,
        y_pred,
        target_names=target_names,
        output_dict=True,
        zero_division=0,
    )
