<!-- Báo cáo lỗi ML: Data Leakage, tràn RAM, Zero-frequency, v.v. -->

## Metadata

| Trường | Giá trị |
|--------|---------|
| **Mức độ** | Blocker / Critical / Major / Minor |
| **Thành phần** | data / features / models / demo / notebooks / CI |
| **Nhãn gợi ý** | `type::bug`, `bug::leakage`, `bug::oom`, `bug::zero-freq` |

## Tóm tắt

<!-- Một câu mô tả lỗi -->



## Phân loại lỗi (chọn)

- [ ] **Data Leakage** — thông tin Test/Val lọt vào Train / fit vectorizer sai tập
- [ ] **Tràn RAM (OOM)** — TF-IDF / RF / load toàn bộ corpus
- [ ] **Zero-frequency (Naive Bayes)** — từ chưa thấy ở Train → xác suất 0 / log(0)
- [ ] **Mất cân bằng lớp / metric sai** — average, `pos_label`, stratified split lệch
- [ ] **Khác:**

## Môi trường tái hiện

| Mục | Giá trị |
|-----|---------|
| OS | |
| Python | |
| Nhánh / commit | |
| Dataset / split | |
| Notebook / script | |

## Các bước tái hiện

1.
2.
3.

## Kết quả mong đợi



## Kết quả thực tế

```
# dán traceback / log / số liệu bất thường
```

## Ảnh hưởng

- [ ] Chặn pipeline dữ liệu
- [ ] Chặn huấn luyện / đánh giá
- [ ] Làm sai số liệu báo cáo / slides
- [ ] Demo Streamlit không chạy

## Hướng khắc phục đề xuất (nếu có)

<!-- Ví dụ: Laplace alpha > 0; giảm max_features; fit TF-IDF chỉ trên train; sparse matrix... -->



## Đính kèm

- Log / screenshot / đường dẫn file liên quan:
