"""Ghi nhận log thực thi và kiểm soát tiến trình chạy."""

from __future__ import annotations

import logging
import sys
from typing import Optional


_CONFIGURED = False


def setup_logging(
    level: int = logging.INFO,
    *,
    fmt: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
) -> None:
    """Cấu hình root logger một lần cho toàn dự án."""
    global _CONFIGURED
    if _CONFIGURED:
        return

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    root = logging.getLogger()
    root.setLevel(level)
    if not root.handlers:
        root.addHandler(handler)
    _CONFIGURED = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Trả về logger theo tên module; tự gọi ``setup_logging`` nếu chưa cấu hình."""
    if not _CONFIGURED:
        setup_logging()
    return logging.getLogger(name or "spam_filtering_ml")
