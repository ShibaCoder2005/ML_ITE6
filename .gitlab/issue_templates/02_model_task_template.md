<!-- Đội 2 — Huấn luyện MNB, SVM, Random Forest -->

## Metadata

| Trường | Giá trị |
|--------|---------|
| **Đội** | Đội 2 — Modeling |
| **Loại** | Task / Story |
| **Ưu tiên** | Low / Medium / High |
| **Milestone** | |
| **Nhãn gợi ý** | `team::model`, `algo::mnb`, `algo::svm`, `algo::rf` |
| **Mô hình** | Multinomial NB / SVM / Random Forest |

## Mục tiêu

<!-- Ví dụ: quét alpha Laplace cho MNB trên Val; lưu checkpoint tốt nhất -->



## Phạm vi công việc

- [ ] Dùng **chỉ** `train.csv` để fit vectorizer + model
- [ ] Dùng `val.csv` để tinh chỉnh siêu tham số
- [ ] **Không** đụng `test.csv` trong giai đoạn này
- [ ] Cập nhật module tương ứng trong `src/models/`
- [ ] Cập nhật notebook (`03_modeling_naive_bayes` / `04_modeling_svm` / `05_modeling_random_forest`)
- [ ] Lưu checkpoint vào `saved_models/` (local; không commit `.pkl` nặng)

## Siêu tham số khảo sát

| Tham số | Khoảng giá trị | Kết quả tốt nhất (Val) |
|---------|----------------|------------------------|
| | | |

## Metric trên Val (điền sau khi chạy)

| Metric | Giá trị |
|--------|---------|
| Accuracy | |
| Precision | |
| Recall | |
| F1 | |

## Definition of Done

- [ ] Có bảng so sánh cấu hình trên Val
- [ ] Checkpoint tái tạo được từ seed + config đã ghi
- [ ] Code module hóa, không hard-code path tuyệt đối máy cá nhân
- [ ] Không data leakage (vectorizer chỉ fit trên Train)

## Liên kết

- Phụ thuộc bàn giao dữ liệu (Issue/MR Đội 1):
- Issue đánh giá tiếp theo:

## Ghi chú / rủi ro

<!-- Tràn RAM, thời gian train, mất cân bằng lớp, Zero-frequency (NB)... -->


