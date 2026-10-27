"""Ứng dụng web tương tác thời gian thực (Streamlit) — demo lọc spam."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = ROOT / "saved_models"
SAMPLES_PATH = Path(__file__).parent / "demo_samples.txt"


def _load_artifacts():
    """Tải vectorizer + mô hình nếu đã có checkpoint."""
    try:
        import joblib
    except ImportError:
        return None, None, "Thiếu joblib. Cài: pip install -r requirements.txt"

    vec_path = MODELS_DIR / "tfidf_vectorizer.pkl"
    # Ưu tiên MNB, fallback SVM
    model_path = MODELS_DIR / "mnb_best_model.pkl"
    if not model_path.exists():
        model_path = MODELS_DIR / "svm_best_model.pkl"

    if not vec_path.exists() or not model_path.exists():
        return None, None, (
            "Chưa có checkpoint trong `saved_models/`. "
            "Hãy huấn luyện mô hình (notebooks 03–05) rồi lưu `.pkl`."
        )

    vectorizer = joblib.load(vec_path)
    model = joblib.load(model_path)
    return vectorizer, model, None


def _load_samples() -> list[str]:
    if not SAMPLES_PATH.exists():
        return []
    lines = SAMPLES_PATH.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")]


def main() -> None:
    st.set_page_config(page_title="Spam Filter Demo", page_icon="✉", layout="centered")
    st.title("Spam Filtering Demo")
    st.caption("Phân loại tin nhắn / email: Spam vs Ham")

    vectorizer, model, err = _load_artifacts()
    if err:
        st.warning(err)

    samples = _load_samples()
    default = samples[0] if samples else ""
    if samples:
        choice = st.selectbox("Mẫu demo", ["(tự nhập)"] + samples)
        if choice != "(tự nhập)":
            default = choice

    text = st.text_area("Nội dung cần kiểm tra", value=default, height=160)

    if st.button("Phân loại", type="primary"):
        if not text.strip():
            st.error("Vui lòng nhập nội dung.")
        elif vectorizer is None or model is None:
            st.error("Không thể dự đoán vì thiếu mô hình đã huấn luyện.")
        else:
            X = vectorizer.transform([text])
            pred = model.predict(X)[0]
            label = str(pred)
            if label.lower() in {"spam", "1", "true"}:
                st.error(f"Kết quả: **SPAM** (`{label}`)")
            else:
                st.success(f"Kết quả: **HAM** (`{label}`)")


if __name__ == "__main__":
    main()
