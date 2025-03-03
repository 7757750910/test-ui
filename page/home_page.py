import time
import allure
from configs.element import Element
from base.base import Base
from page.biaodanshejiqi_page import BiaoDansj


class HomePage(Base):

    def __init__(self, base: Base):
        # 不再在此处创建 WebDriver，而是通过传入已经初始化的 base 实例
        self.base = base

    def homepage_biaodansheijiqi(self):
        with allure.step("点击应用配置"):
            self.base.find_click(*Element.HOME_yingyongpeizhi)

        with allure.step("点击引擎管理"):
            self.base.find_click(*Element.YYPZ_yingqinguanli)

        with allure.step("点击表单引擎"):
            self.base.find_click(*Element.YYPZ_YQGL_biaodanyinqing)

        with allure.step("点击表单设计器"):
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_biaodanshejiqi)
            time.sleep(1)

        with allure.step("点击新增按钮，进入表单设计--基础信息页面"):
            self.base.driver.save_screenshot("../reports/result/YYPZ_YQGL_BDYQ_biaodanshejiqi.png")
            allure.attach.file("../reports/result/YYPZ_YQGL_BDYQ_biaodanshejiqi.png",
                               attachment_type=allure.attachment_type.PNG)
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_BDSJQ_add)

        return BiaoDansj(self.base)
