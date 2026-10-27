# Đặc tả bài toán — Lọc thư rác (Spam Filtering)

## 1. Bối cảnh

Lọc thư rác là bài toán phân loại văn bản nhị phân: gán nhãn **Spam** hoặc **Ham** cho tin nhắn/email dựa trên nội dung.

## 2. Phát biểu (T, P, E)

### T — Task

Học hàm $h: \mathcal{X} \rightarrow \mathcal{Y}$ với:

- $\mathcal{X}$: không gian văn bản (sau tiền xử lý, biểu diễn TF-IDF)
- $\mathcal{Y} = \{\text{spam}, \text{ham}\}$

### P — Performance

Đánh giá trên **test set độc lập**:

| Metric | Vai trò |
|--------|---------|
| Accuracy | Tổng quan đúng/sai |
| Precision | Giảm False Positive (ham bị gắn spam) |
| Recall | Giảm False Negative (bỏ sót spam) |
| F1-score | Cân bằng Precision–Recall |
| Confusion Matrix | Phân tích FP / FN |

Ưu tiên nghiệp vụ: hạn chế **False Negative** (spam lọt vào hộp thư).

### E — Experience

Tập dữ liệu gắn nhãn (ví dụ SMS Spam Collection / spam.csv):

- Chia **stratified** Train / Val / Test = **60% / 20% / 20%**
- Vectorizer và mô hình chỉ fit trên Train; Val dùng tinh chỉnh siêu tham số; Test chỉ đánh giá lần cuối

## 3. Pipeline tóm tắt

1. Làm sạch văn bản (`src/data/cleaner.py`)
2. TF-IDF (`src/features/vectorizer.py`)
3. Mô hình: MNB, SVM, Random Forest (`src/models/`)
4. Đánh giá & phân tích lỗi (`docs/error_analysis_report.md`)
