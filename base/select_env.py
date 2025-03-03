import os

import yaml


class SelectEnv:
    @staticmethod
    def select_env():
        # 获取默认环境变量
        # 使用os.getenv()函数获取名为"env"的环境变量的值。如果该环境变量未设置，则使用"default"参数指定的默认值"env_test"。
        default = os.getenv("env", default="env_dev")
        # 加载YAML文件
        # 使用yaml.safe_load()函数从文件中加载YAML数据。文件名是根据上一步获取的default变量动态构建的，假设"env_dev.yaml"是一个存在的文件名
        # 获取当前脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 拼接配置文件的绝对路径
        config_path = os.path.join(current_dir, '../configs', f'{default}.yaml')
        # 加载YAML配置文件
        data = yaml.safe_load(open(config_path, encoding="UTF-8"))

        # 存储配置数据
        # 将加载的YAML数据存储在env属性中，以便后续访问 {'base_url': 'http://172.16.42.215/api/admin'}
        env = data
        # 从加载的配置数据中获取env字典中的"base_url"键的值，并将其存储在base_url属性中
        base_url = env["base_url"]
        user_name = env["user_name"]
        password = env["password"]

        return base_url, user_name, password
