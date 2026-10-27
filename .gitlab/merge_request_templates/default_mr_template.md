<!-- Mẫu Merge Request chuẩn — tích hợp checklist review code -->

## Summary

<!-- 1–3 câu: thay đổi gì và tại sao -->



## Loại thay đổi

- [ ] Feature / task mới
- [ ] Bug fix
- [ ] Refactor / dọn code
- [ ] Docs / slides
- [ ] Notebook thực nghiệm
- [ ] Khác:

## Liên kết Issue

Closes #

## Thay đổi chính

-
-
-

## Checklist — tác giả

- [ ] Code chạy được trên máy local với hướng dẫn trong `README.md`
- [ ] Không commit `.pkl` nặng, dữ liệu thô lớn, hay secrets (`.env`)
- [ ] Không data leakage (fit chỉ trên Train; Test chỉ đánh giá cuối)
- [ ] Seed / config siêu tham số được ghi lại nếu ảnh hưởng kết quả
- [ ] Đã cập nhật notebook / docs liên quan (nếu cần)
- [ ] Self-review diff trước khi mở MR

## Checklist — reviewer

- [ ] Logic đúng với mục tiêu Issue
- [ ] Đặt tên / cấu trúc module nhất quán với `src/`
- [ ] Không hard-code path tuyệt đối máy cá nhân
- [ ] Metric / split được mô tả rõ nếu có thay đổi pipeline
- [ ] An toàn: không lộ credential; `.gitignore` vẫn hiệu lực

## Kế hoạch kiểm thử

- [ ] Unit / chạy tay module bị ảnh hưởng
- [ ] Notebook liên quan chạy end-to-end (nếu có)
- [ ] Demo Streamlit vẫn mở được (nếu đụng `demo/` hoặc checkpoint)

## Ghi chú cho reviewer


