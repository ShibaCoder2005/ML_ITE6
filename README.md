# Spam Filtering ML

Hệ thống lọc thư rác (Spam/Ham) dựa trên học máy có giám sát: TF-IDF + Multinomial Naive Bayes / SVM / Random Forest.

## Phát biểu bài toán (T, P, E)

| Thành phần | Mô tả |
|------------|--------|
| **T (Task)** | Phân loại nhị phân tin nhắn/email thành Spam hoặc Ham |
| **P (Performance)** | Accuracy, Precision, Recall, F1-score; ưu tiên giảm False Negative (bỏ sót spam) |
| **E (Experience)** | Tập dữ liệu gắn nhãn Spam/Ham (ví dụ SMS Spam Collection), chia Train/Val/Test phân tầng 60/20/20 |

Chi tiết: [`docs/problem_formulation.md`](docs/problem_formulation.md).

## Cấu trúc dự án

```
spam-filtering-ml/
├── data/           # raw → processed → splits
├── notebooks/      # EDA → preprocessing → modeling → evaluation
├── src/            # module tái sử dụng (data, features, models, utils)
├── saved_models/   # checkpoint TF-IDF + mô hình tốt nhất
├── demo/           # ứng dụng Streamlit
├── docs/           # SRS, phân tích lỗi
└── presentation/   # slides & figures
```

## Cài đặt

```bash
cd spam-filtering-ml
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Đặt dữ liệu thô vào `data/raw/` (ví dụ `spam.csv`).

## Tái lập thực nghiệm

1. Chạy lần lượt notebook trong `notebooks/` (01 → 06), **hoặc** dùng pipeline trong `src/`.
2. Checkpoint tốt nhất lưu vào `saved_models/`.
3. Demo:

```bash
streamlit run demo/app.py
```

## License / ghi chú môn học

Dự án phục vụ bài tập / báo cáo môn học. Cập nhật tài liệu trong `docs/` và `presentation/` theo tiến độ nhóm.
