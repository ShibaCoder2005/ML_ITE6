# Software Requirements Specification (SRS) v1.0

**Hệ thống:** Spam Filtering ML  
**Chuẩn tham chiếu:** IEEE 830 (rút gọn cho dự án môn học)  
**Phiên bản:** 1.0  

---

## 1. Introduction

### 1.1 Purpose

Đặc tả yêu cầu chức năng và phi chức năng cho hệ thống phân loại Spam/Ham, phục vụ huấn luyện, đánh giá và demo thuyết trình.

### 1.2 Scope

- Pipeline dữ liệu: raw → processed → splits  
- Huấn luyện / so sánh: Multinomial NB, SVM, Random Forest  
- Demo tương tác (Streamlit)  
- **Ngoài phạm vi:** triển khai production mail server, real-time streaming quy mô lớn  

### 1.3 Definitions

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| Spam | Thư/tin không mong muốn, quảng cáo, lừa đảo |
| Ham | Thư/tin hợp lệ |
| TF-IDF | Term Frequency–Inverse Document Frequency |
| Stratified split | Chia tập giữ tỷ lệ nhãn |

---

## 2. Overall description

### 2.1 Product perspective

Hệ thống offline / batch học máy + ứng dụng demo web cục bộ.

### 2.2 User classes

| Người dùng | Nhu cầu |
|------------|---------|
| Nhóm Data | Chuẩn bị & kiểm soát chất lượng dữ liệu |
| Nhóm ML | Huấn luyện, tinh chỉnh, đánh giá |
| Người thuyết trình | Demo phân loại thời gian thực |

---

## 3. Specific requirements

### 3.1 Functional requirements

| ID | Yêu cầu |
|----|---------|
| FR-01 | Hệ thống phải đọc được CSV dữ liệu thô có cột văn bản và nhãn |
| FR-02 | Hệ thống phải làm sạch văn bản (chữ thường, loại nhiễu, stop-words) |
| FR-03 | Hệ thống phải chia Train/Val/Test phân tầng 60/20/20 |
| FR-04 | Hệ thống phải biểu diễn văn bản bằng TF-IDF |
| FR-05 | Hệ thống phải huấn luyện ít nhất MNB, SVM, Random Forest |
| FR-06 | Hệ thống phải báo cáo Accuracy, Precision, Recall, F1, Confusion Matrix trên Test |
| FR-07 | Demo phải nhận văn bản đầu vào và trả nhãn Spam/Ham nếu đã có checkpoint |

### 3.2 Non-functional requirements

| ID | Yêu cầu |
|----|---------|
| NFR-01 | Mã nguồn module hóa dưới `src/` |
| NFR-02 | Thực nghiệm tái lập được qua notebook / seed cố định |
| NFR-03 | File `.pkl` nặng không commit vào Git (xem `.gitignore`) |
| NFR-04 | Tài liệu (T,P,E) và SRS nằm trong `docs/` |

---

## 4. Appendices

Cập nhật khi nhóm chốt dataset, metric ưu tiên và mô hình production-demo cuối cùng.
