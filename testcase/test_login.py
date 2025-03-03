import logging
import allure
from base.base import Base

from page.login_page import LoginPage


# 测试登录
class TestLoginPage:
    def setup_class(self):
        self.base = Base()
        self.login = LoginPage(self.base)

    @allure.story("登录")
    @allure.title("测试 登录页面 ")
    def test_login(self):
        logging.info('开始 测试 登录页面')
        r = self.login.login_page()
        logging.info('测试 登录页面 完成')
        assert "欢迎回来" in r[0]

    def teardown_class(self):
        # 测试结束后关闭浏览器
        self.base.quit()
