# Churn Prediction Model

## Giới thiệu

Dự án được thực hiện nhằm dự đoán khách hàng có nguy cơ rời bỏ (churn) trong 30 ngày tới để hỗ trợ đội Sales chủ động chăm sóc và giữ chân khách hàng.

Mô hình sử dụng dữ liệu giao dịch thực tế và áp dụng Logistic Regression để tính xác suất churn cho từng khách hàng.

---

## Công nghệ sử dụng

* Python
* Pandas
* Scikit-learn
* Openpyxl

Cài đặt thư viện:

```bash
pip install pandas scikit-learn openpyxl
```

---

## Dataset sử dụng

File dữ liệu: `ver1.xlsx`
Sheet sử dụng: `Data Model`

Các cột chính:

* Khách hàng
* Ngày Xuất
* Doanh Thu
* Lợi Nhuận
* % SL Khuyến mãi
* Segment
* Ngành Hàng

---

## Quy trình thực hiện

### 1. Đọc và xử lý dữ liệu

Dữ liệu được đọc từ Excel bằng pandas, sau đó chuẩn hóa cột ngày và xử lý dữ liệu thiếu.

### 2. Feature Engineering

Xây dựng các đặc trưng cho từng khách hàng:

* Recency: số ngày từ lần mua cuối
* Frequency: số lần mua
* AOV: doanh thu trung bình
* Promo Rate: tỷ lệ khuyến mãi trung bình
* Margin: tỷ lệ lợi nhuận

### 3. Tạo nhãn churn

Khách hàng được gán:

* Churn = 1 nếu hơn 30 ngày chưa mua
* Churn = 0 nếu còn hoạt động

### 4. Build model

Sử dụng Logistic Regression kết hợp StandardScaler để huấn luyện mô hình và dự đoán xác suất churn.

### 5. Phân loại mức độ

Khách hàng được chia thành:

* Khẩn cấp
* Cao
* Trung bình

### 6. Đề xuất hành động

Dựa trên Recency và Segment:

* VIP → Gặp mặt
* > 60 ngày → Gọi ngay
* > 30 ngày → Zalo offer

---

## Kết quả đạt được

Mô hình giúp:

* Xác định khách hàng có nguy cơ churn cao
* Hỗ trợ Sales ưu tiên chăm sóc đúng khách hàng
* Tăng khả năng giữ chân khách hàng

Output cuối cùng được xuất ra file:

```text
churn_list.xlsx
```

---

## Cách chạy project

```bash
python process.py
```

Sau khi chạy thành công, hệ thống sẽ tự động tạo file `churn_list.xlsx`.
