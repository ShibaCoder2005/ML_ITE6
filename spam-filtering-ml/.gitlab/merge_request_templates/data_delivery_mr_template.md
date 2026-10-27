<!-- Mẫu MR bàn giao dữ liệu: Đội 1 → Đội 2 (kiểm soát phân tầng) -->

## Summary

Bàn giao bộ dữ liệu đã làm sạch và chia **stratified** Train/Val/Test cho Đội Modeling.

## Metadata bàn giao

| Trường | Giá trị |
|--------|---------|
| **Từ** | Đội 1 — Data |
| **Đến** | Đội 2 — Modeling |
| **Nguồn thô** | `data/raw/...` |
| **Processed** | `data/processed/...` |
| **Splits** | `data/splits/{train,val,test}.csv` |
| **Tỷ lệ** | 60% / 20% / 20% |
| **`random_state`** | |
| **Issue liên quan** | # |

## Kiểm soát phân tầng (bắt buộc)

| Tập | Số mẫu | % Spam | % Ham |
|-----|--------|--------|-------|
| Train | | | |
| Val | | | |
| Test | | | |
| **Toàn bộ** | | | |

- [ ] Tỷ lệ nhãn giữa các tập lệch trong ngưỡng chấp nhận (ghi rõ ngưỡng, ví dụ ≤ 1–2 điểm %)
- [ ] Không chồng chéo mẫu giữa train / val / test (kiểm tra hash / id nếu có)
- [ ] Schema thống nhất: cột `text`, `label`
- [ ] Không giá trị `text` rỗng sau cleaner (hoặc đã được loại có chủ đích)

## Chống Data Leakage

- [ ] Test **không** dùng để chọn tham số làm sạch / từ vựng
- [ ] Stop-words / quy tắc cleaner cố định hoặc chỉ ước lượng trên Train
- [ ] Hướng dẫn Đội 2: fit TF-IDF **chỉ** trên Train; Val tinh chỉnh; Test đánh giá cuối

## Artefact kèm theo

- [ ] Notebook EDA / preprocess đã cập nhật (`01`, `02`)
- [ ] Ghi chú quyết định tiền xử lý (trong MR hoặc `docs/`)
- [ ] (Tuỳ chọn) checksum / số dòng file để đối chiếu

```
# ví dụ
wc -l data/splits/*.csv
```

## Checklist review (Đội 2 xác nhận)

- [ ] Đọc được splits bằng `src.data.loader` / pandas
- [ ] Phân bố lớp khớp bảng trên
- [ ] Sẵn sàng bắt đầu Issue modeling (MNB / SVM / RF)

## Ghi chú / rủi ro còn lại


