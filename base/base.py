from base.select_env import SelectEnv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Base:
    _URL = SelectEnv.select_env()[0]

    def __init__(self):
        """初始化webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # 启动时最大化
        chrome_options.add_argument("--disable-extensions")  # 禁用扩展
        chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速
        # chrome_options.add_argument("--headless")  # 如果需要无头模式，可以取消注释此行
        self.driver = webdriver.Chrome(options=chrome_options)
        # 设置全局隐形等待时间（10 秒）
        self.driver.implicitly_wait(10)
        """打开指定的 URL"""
        self.driver.get(self._URL)
        # 刷新当前页面
        self.driver.refresh()
        logging.info("页面已打开并刷新")

    def find(self, by, value, timeout=10):
        """查找单个元素并进行显式等待"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            logging.info(f"查找元素失败: {e}")
            return None

    def finds(self, by, value, timeout=10):
        """查找多个元素并进行显式等待"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            return elements
        except Exception as e:
            logging.info(f"查找元素失败: {e}")
            return []

    def find_click(self, by, value, timeout=10):
        """查查找元素并点击，输出详细日志"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            logging.info(f"成功找到并点击元素: {by}, {value}, 当前页面标题: {self.driver.title}")
            element.click()
            return element
        except Exception as e:
            logging.error(f"发生意外错误: {e}")
            return None

    def find_send(self, by, value, keys, timeout=10):
        """查找元素并输入文本，输出详细日志"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            logging.info(f"成功找到并输入元素: {by}, {value}, 当前页面标题: {self.driver.title}")
            element.send_keys(keys)
            return element
        except Exception as e:
            logging.error(f"发生意外错误: {e}")
            return None

    def find_click_hold(self, by, value, timeout=10):
        """鼠标点击并按住不放，输出详细日志"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            logging.info(f"成功找到并点击元素: {by}, {value}, 当前页面标题: {self.driver.title}")
            # 使用 ActionChains 来点击并按住
            actions = ActionChains(self.driver)
            actions.click_and_hold(element).perform()
            # 返回已经点击并按住的元素
            return element
        except Exception as e:
            logging.error(f"发生意外错误: {e}")
            return None

    def drag_and_drop(self, source_by, source_value, target_by, target_value, timeout=10):
        """拖动元素从源位置到目标位置，并输出详细日志"""
        try:
            # 等待源元素和目标元素可点击
            source_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((source_by, source_value))
            )
            logging.info(f"成功找到源元素: {source_by}, {source_value}, 当前页面标题: {self.driver.title}")

            target_element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((target_by, target_value))
            )
            logging.info(f"成功找到目标元素: {target_by}, {target_value}, 当前页面标题: {self.driver.title}")

            # 使用 ActionChains 来执行拖动操作
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_element, target_element).perform()

            logging.info(f"成功将元素从 {source_by}, {source_value} 拖动到 {target_by}, {target_value}")
            return source_element
        except Exception as e:
            # 捕捉异常并输出详细日志
            logging.error(f"发生意外错误: {e}")
            return None

    def win_han(self):
        a = self.driver.window_handles
        print(a)

    def quit(self):
        """退出浏览器"""
        self.driver.quit()
        logging.info("退出浏览器")
