import time
import allure
from base.select_env import SelectEnv
from configs.element import Element
from base.base import Base
from page.home_page import HomePage


class LoginPage(Base):
    _User_name = SelectEnv.select_env()[1]
    _Password = SelectEnv.select_env()[2]

    def __init__(self, base: Base):
        # 不再在此处创建 WebDriver，而是通过传入已经初始化的 base 实例
        self.base = base

    def login_page(self):
        with allure.step("点击租户选择下拉框"):
            self.base.find(*Element.LOGIN_laxiajiantou).click()
            time.sleep(1)

        with allure.step("选择中核华辉租户"):
            self.base.find(*Element.LOGIN_xuanzezuhu).click()
            time.sleep(2)

        with allure.step("输入用户名,输入密码"):
            self.base.finds(*Element.LOGIN_shuruzhanghao)[0].send_keys(self._User_name)
            self.base.finds(*Element.LOGIN_shuruzhanghao)[1].send_keys(self._Password)
            time.sleep(1)

        with allure.step("点击登录按钮"):
            self.base.find(*Element.LOGIN_denglu).click()
            time.sleep(3)

        with allure.step("获取登录成功提示并进行截图"):
            a = self.base.find(*Element.LOGIN_dengluxinxi).text
            self.base.driver.save_screenshot("../reports/result/LOGIN_dengluxinxi.png")
            allure.attach.file("../reports/result/LOGIN_dengluxinxi.png", attachment_type=allure.attachment_type.PNG)

        # 返回 登录成功提示语 & HomePage 实例
        return a, HomePage(self.base)
