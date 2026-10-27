<!-- Đội 1 — Thu thập, EDA, Tiền xử lý dữ liệu -->

## Metadata

| Trường | Giá trị |
|--------|---------|
| **Đội** | Đội 1 — Data |
| **Loại** | Task / Story |
| **Ưu tiên** | Low / Medium / High |
| **Milestone** | |
| **Nhãn gợi ý** | `team::data`, `stage::eda`, `stage::preprocess` |

## Mục tiêu

<!-- Mô tả ngắn: thu thập / EDA / làm sạch / chia split -->



## Phạm vi công việc

- [ ] Thu thập / xác thực dữ liệu thô (`data/raw/`)
- [ ] EDA: phân bố lớp Spam/Ham, độ dài văn bản, giá trị thiếu
- [ ] Tiền xử lý: chuẩn hóa chữ thường, khử nhiễu, stop-words (`src/data/cleaner.py`)
- [ ] Lưu dữ liệu đã làm sạch (`data/processed/`)
- [ ] Stratified split 60/20/20 → `data/splits/{train,val,test}.csv`
- [ ] Cập nhật notebook liên quan (`01_eda_...`, `02_preprocessing_...`)
- [ ] Ghi chú quyết định vào `docs/` (nếu có)

## Đầu vào / Đầu ra

| | Mô tả |
|--|--------|
| **Input** | |
| **Output** | |
| **Definition of Done** | File đúng path, tỷ lệ nhãn được kiểm chứng, không data leakage |

## Kiểm soát chất lượng dữ liệu

- [ ] Schema cột thống nhất (`text`, `label`)
- [ ] Không dòng trùng lặp bất thường giữa train/val/test
- [ ] Tỷ lệ Spam/Ham gần như bảo toàn sau stratified split
- [ ] Seed / `random_state` được ghi lại để tái lập

## Liên kết

- Issue liên quan:
- MR bàn giao (dùng template `data_delivery_mr_template`):

## Ghi chú thêm


