import logging
import allure
from base.base import Base
from page.login_page import LoginPage


# 测试登录
class TestLoginPage:
    def setup_class(self):
        self.base = Base()
        self.login = LoginPage(self.base)

    @allure.story("应用配置-引擎管理-表单引擎-表单设计器")
    @allure.title("测试 新增表单 ")
    def test_add_biaodan(self):
        logging.info('开始 测试 新增表单')
        r = self.login.login_page()[1].homepage_biaodansheijiqi().biaodansheji()
        logging.info('测试 新增表单 完成')
        assert "保存成功" == r

    def teardown_class(self):
        # 测试结束后关闭浏览器
        self.base.quit()
