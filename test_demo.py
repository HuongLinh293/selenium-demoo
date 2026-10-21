import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo:
    def setup_method(self):
        """Khởi tạo trình duyệt Chrome và truy cập website trước mỗi test case"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        """Đóng trình duyệt sau khi kết thúc từng test case"""
        self.driver.quit()

    def test_tc01_login_success(self):
        """TC01: Đăng nhập thành công với tài khoản hợp lệ"""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Xác minh tiêu đề trang hiển thị "Products"
        title = self.driver.find_element(By.CLASS_NAME, "title").text
        assert title == "Products"

    def test_tc02_login_failure(self):
        """TC02: Đăng nhập thất bại khi nhập sai mật khẩu"""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Xác minh thông báo lỗi hiển thị
        error_msg = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Username and password do not match" in error_msg

    def test_tc03_sort_products(self):
        """TC03: Sắp xếp sản phẩm theo giá từ thấp đến cao"""
        # Đăng nhập
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Chọn bộ lọc "Price (low to high)"
        sort_select = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_select.click()
        self.driver.find_element(By.XPATH, "//option[@value='lohi']").click()
        
        # Xác minh sản phẩm đầu tiên có giá thấp nhất ($7.99)
        first_price = self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert first_price == "$7.99"

    def test_tc04_add_to_cart(self):
        """TC04: Thêm sản phẩm vào giỏ hàng"""
        # Đăng nhập
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Thêm món hàng "Sauce Labs Backpack" vào giỏ
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        # Xác minh biểu tượng giỏ hàng cập nhật số lượng là 1
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == "1"

    def test_tc05_logout(self):
        """TC05: Đăng xuất khỏi hệ thống thành công"""
        # Đăng nhập
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Nhấn mở Side Menu và chọn Logout
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_btn.click()
        
        # Chờ 1 giây để trang điều hướng hoàn tất
        time.sleep(1)
        
        # Xác minh quay lại trang đăng nhập bằng cách kiểm tra URL hoặc ô nhập username
        current_url = self.driver.current_url
        assert "saucedemo.com" in current_url
        assert self.driver.find_element(By.ID, "user-name").is_displayed()
