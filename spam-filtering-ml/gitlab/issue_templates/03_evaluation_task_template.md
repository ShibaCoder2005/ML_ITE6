<!-- Đội 2 — Đo lường Performance, Confusion Matrix trên Test -->

## Metadata

| Trường | Giá trị |
|--------|---------|
| **Đội** | Đội 2 — Evaluation |
| **Loại** | Task / Story |
| **Ưu tiên** | Low / Medium / High |
| **Milestone** | |
| **Nhãn gợi ý** | `team::model`, `stage::eval`, `report` |

## Mục tiêu

Đánh giá **độc lập** trên Test set: Accuracy, Precision, Recall, F1 và Confusion Matrix; phân tích FP/FN.

## Phạm vi công việc

- [ ] Load checkpoint tốt nhất + `tfidf_vectorizer.pkl`
- [ ] Transform `test.csv` (không re-fit)
- [ ] Tính metrics (`src/models/evaluate.py`)
- [ ] Vẽ / lưu Confusion Matrix vào `presentation/figures/`
- [ ] Chạy notebook `06_evaluation_benchmark.ipynb`
- [ ] Điền `docs/error_analysis_report.md` (mẫu FP / FN)
- [ ] So sánh MNB vs SVM vs Random Forest (bảng tổng hợp)

## Bảng kết quả trên Test (P)

| Mô hình | Accuracy | Precision | Recall | F1 |
|---------|----------|-----------|--------|-----|
| MNB | | | | |
| SVM | | | | |
| Random Forest | | | | |

## Confusion Matrix

<!-- Dán bảng hoặc link ảnh trong presentation/figures/ -->

|  | Pred Ham | Pred Spam |
|--|----------|-----------|
| **True Ham** | TN | FP |
| **True Spam** | FN | TP |

## Phân tích nhanh

- **False Positive (Ham → Spam):** nguyên nhân giả thuyết
- **False Negative (Spam → Ham):** nguyên nhân giả thuyết
- **Mô hình đề xuất cho demo:** lý do (trade-off Precision/Recall)

## Definition of Done

- [ ] Chỉ đánh giá Test **một lần** sau khi chốt siêu tham số trên Val
- [ ] Báo cáo lỗi có ít nhất vài mẫu FP/FN điển hình
- [ ] Figure/metrics đủ dùng cho slides thuyết trình

## Liên kết

- Issue huấn luyện liên quan:
- MR / commit chứa số liệu:

## Ghi chú thêm


