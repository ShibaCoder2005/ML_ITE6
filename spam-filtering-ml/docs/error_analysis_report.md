# Báo cáo phân tích lỗi dự đoán (Error Analysis)

> Điền sau khi chạy notebook `06_evaluation_benchmark.ipynb` trên **test set**.

## 1. Tổng quan

| Mục | Giá trị |
|-----|---------|
| Mô hình đánh giá | _TBD_ |
| Test size | _TBD_ |
| Accuracy | _TBD_ |
| Precision (spam) | _TBD_ |
| Recall (spam) | _TBD_ |
| F1 (spam) | _TBD_ |

### Confusion Matrix (schema)

|  | Pred Ham | Pred Spam |
|--|----------|-----------|
| **True Ham** | TN | FP |
| **True Spam** | FN | TP |

## 2. False Positive (Ham → Spam)

**Định nghĩa:** tin hợp lệ bị gắn nhãn spam.

### Mẫu điển hình

| # | Nội dung (rút gọn) | Giả thuyết nguyên nhân |
|---|--------------------|------------------------|
| 1 | _TBD_ | Từ khóa “free”, “win”, URL… xuất hiện trong ngữ cảnh hợp lệ |
| 2 | _TBD_ | _TBD_ |

### Hướng cải thiện

- Điều chỉnh ngưỡng quyết định / `class_weight`
- Mở rộng n-gram hoặc đặc trưng meta (độ dài, tỷ lệ chữ hoa)
- Review stop-words / từ gây nhiễu

## 3. False Negative (Spam → Ham)

**Định nghĩa:** spam bị bỏ sót (nguy hiểm hơn về mặt bảo mật hộp thư).

### Mẫu điển hình

| # | Nội dung (rút gọn) | Giả thuyết nguyên nhân |
|---|--------------------|------------------------|
| 1 | _TBD_ | Từ vựng mới / obfuscation (ký tự lạ, khoảng trắng) |
| 2 | _TBD_ | Spam ngắn, ít tín hiệu TF-IDF |

### Hướng cải thiện

- Tăng Recall: giảm `C` / tinh chỉnh `alpha`, cân bằng lớp
- Bổ sung quy tắc heuristic (URL rút gọn, số điện thoại)
- Thu thập thêm mẫu spam tương tự (data augmentation nhẹ)

## 4. Kết luận

_TBD — tóm tắt trade-off Precision vs Recall và mô hình chọn cho demo._
