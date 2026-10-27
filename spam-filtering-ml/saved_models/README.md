# saved_models

Sau khi huấn luyện, lưu các checkpoint tại đây (bị `.gitignore` bỏ qua `*.pkl`):

| File | Mô tả |
|------|--------|
| `tfidf_vectorizer.pkl` | Vectorizer đã fit trên Train |
| `mnb_best_model.pkl` | Multinomial NB tối ưu (alpha) |
| `svm_best_model.pkl` | SVM tối ưu (C / kernel) |

Không commit file nặng; tái tạo bằng notebook `03`–`05`.
