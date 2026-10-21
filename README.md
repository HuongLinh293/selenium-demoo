


# Báo Cáo Kiểm Thử Tự Động Với Selenium WebDriver

## 1. Thông tin chung
- **Họ và tên:** [Tên của bạn]
- **Mã sinh viên / Lớp:** [Mã số của bạn]
- **Website kiểm thử:** [SauceDemo](https://www.saucedemo.com/)
- **Công cụ / Ngôn ngữ:** Python 3, Selenium WebDriver, Pytest

---

## 2. Kịch bản Kiểm thử (05 Test Cases)

| STT | Mã TC | Tên Test Case | Các bước thực hiện | Kết quả mong đợi |
|-----|-------|---------------|-------------------|------------------|
| 1 | TC01 | Đăng nhập thành công | 1. Nhập username `standard_user`<br>2. Nhập password `secret_sauce`<br>3. Nhấn "Login" | Chuyển hướng đến trang sản phẩm, hiển thị tiêu đề "Products". |
| 2 | TC02 | Đăng nhập thất bại | 1. Nhập username `standard_user`<br>2. Nhập sai password<br>3. Nhấn "Login" | Hiển thị thông báo lỗi "Username and password do not match...". |
| 3 | TC03 | Sắp xếp sản phẩm | 1. Đăng nhập thành công<br>2. Chọn bộ lọc "Price (low to high)" | Danh sách sắp xếp theo giá tăng dần ($7.99 ở đầu). |
| 4 | TC04 | Thêm vào giỏ hàng | 1. Đăng nhập thành công<br>2. Nhấn "Add to cart" sản phẩm Backpack | Icon giỏ hàng hiển thị badge số 1. |
| 5 | TC05 | Đăng xuất | 1. Đăng nhập thành công<br>2. Mở Menu side-bar<br>3. Nhấn "Logout" | Chuyển hướng về trang đăng nhập thành công. |

---

## 3. Cấu trúc Dự án
```text
selenium-demo/
├── test_demo.py    # Chứa toàn bộ 05 test cases tự động
└── README.md       # Báo cáo kiểm # Báo Cáo Kiểm Thử Tự Động Với Selenium WebDriver

## 1. Thông tin chung
- **Họ và tên:** [Ta Thu Huowng Linh]
- **Mã sinh viên / Lớp:** [0324435240]
- **Website kiểm thử:** [SauceDemo](https://www.saucedemo.com/)
- **Công cụ / Ngôn ngữ:** Python 3, Selenium WebDriver, Pytest

---

## 2. Kịch bản Kiểm thử (05 Test Cases)

| STT | Mã TC | Tên Test Case | Các bước thực hiện | Kết quả mong đợi |
|-----|-------|---------------|-------------------|------------------|
| 1 | TC01 | Đăng nhập thành công | 1. Nhập username `standard_user`<br>2. Nhập password `secret_sauce`<br>3. Nhấn "Login" | Chuyển hướng đến trang sản phẩm, hiển thị tiêu đề "Products". |
| 2 | TC02 | Đăng nhập thất bại | 1. Nhập username `standard_user`<br>2. Nhập sai password<br>3. Nhấn "Login" | Hiển thị thông báo lỗi "Username and password do not match...". |
| 3 | TC03 | Sắp xếp sản phẩm | 1. Đăng nhập thành công<br>2. Chọn bộ lọc "Price (low to high)" | Danh sách sắp xếp theo giá tăng dần ($7.99 ở đầu). |
| 4 | TC04 | Thêm vào giỏ hàng | 1. Đăng nhập thành công<br>2. Nhấn "Add to cart" sản phẩm Backpack | Icon giỏ hàng hiển thị badge số 1. |
| 5 | TC05 | Đăng xuất | 1. Đăng nhập thành công<br>2. Mở Menu side-bar<br>3. Nhấn "Logout" | Chuyển hướng về trang đăng nhập thành công. |

---

## 3. Cấu trúc Dự án
```text
selenium-demo/
├── test_demo.py    # Chứa toàn bộ 05 test cases tự động
└── README.md       # Báo cáo kiểm thử

