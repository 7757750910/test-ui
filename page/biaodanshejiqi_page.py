import time
import allure
from configs.element import Element
from base.base import Base


class BiaoDansj(Base):

    def __init__(self, base: Base):
        # 不再在此处创建 WebDriver，而是通过传入已经初始化的 base 实例
        self.base = base

    def biaodansheji(self):
        with allure.step("输入表单名称"):
            self.base.find_send(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_mingcheng, keys="UI自动化测试")

        with allure.step("点击&选择分类"):
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_fenlei)
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_FL_xuanze)

        with allure.step("输入表单说明"):
            self.base.find_send(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_biaodanshuoming, keys="UI自动化测试")
            time.sleep(1)
            self.base.driver.save_screenshot("../reports/result/biaodansheji_jichuxinxi.png")
            allure.attach.file("../reports/result/biaodansheji_jichuxinxi.png",
                               attachment_type=allure.attachment_type.PNG)

        with allure.step("点击下一步，进入表单设计页面"):
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_xiayibu)

        with allure.step("将容器类的【左右布局】拖动至视图中"):
            self.base.drag_and_drop(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_zuoyoubuju,
                                    *Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_shitu)
            time.sleep(1)
            self.base.driver.save_screenshot("../reports/result/YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_zuoyoubuju.png")
            allure.attach.file("../reports/result/YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_zuoyoubuju.png",
                               attachment_type=allure.attachment_type.PNG)

        with allure.step("点击保存按钮，进入表单设计页面"):
            self.base.find_click(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocun)
            time.sleep(1)

        with allure.step("获取保存成功提示并进行截图"):
            a = self.base.find(*Element.YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocunchenggong).text
            time.sleep(1)
            self.base.driver.save_screenshot("../reports/result/YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocunchenggong.png")
            allure.attach.file("../reports/result/YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocunchenggong.png",
                               attachment_type=allure.attachment_type.PNG)
        return a
