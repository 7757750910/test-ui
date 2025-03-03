项目介绍
---

    zhlx_test_ui_oa
    龙信2.0项目ui自动化代码目录
---

目录结构
-----

    base：     存放基础操作，如环境选择，浏览器驱动，方法封装。
    configs：  存放配置文件，比如环境配置（开发、测试、生产等），以及其他需要在不同测试场景下使用的配置信息。元素位置
    page:      存放页面操作逻辑；
    logs:      存放测试执行过程中的日志文件。
    reports:   存放测试报告。
    testcase:  存放具体的测试用例，每个页面的测试用例单独放在一个文件中。


文件说明
--------
    pytest.ini： pytest.ini文件是用于配置pytest测试框架的配置文件，它可以包含各种配置选项来定制测试运行的方式；[pytest]部分：可以设置全局的pytest选项，比如日志级别、测试路径、测试文件匹配模式等。
    run.py： 项目运行
    README.md: 项目的说明文件，介绍项目背景、如何运行测试、目录、文件结构等信息。



代码拉取
-------
通过git（https://zhlxgit.cnecc.com/zhlxtest/zhhh-test-ui-oa.git）拉取代码对应git项目名zhhh-test-ui-oa


本地运行
----------
删除reports目录下的result目录
执行 run.py 文件
执行完成后，打开终端
切换到reports目录
cd  reports
allure serve ./result/

------------

其他
-------------
1、导出 Python 项目所需的安装包到 requirements.txt 文件
------

生成 requirements.txt 文件：执行以下命令，将当前环境中已安装的所有包及其版本信息导出至 requirements.txt 文件中：
pip freeze > requirements.txt
在项目根目录下，执行以下命令安装所有依赖包：
pip install -r requirements.txt

2、离线安装 requirements.txt 文件中的依赖包
--------
步骤 1：在有网络的机器上下载依赖包
假设我们要下载包到一个名为 packages 的目录中。首先，确保当前目录中有你的 requirements.txt 文件，然后运行以下命令：
mkdir packages
pip download  -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt -d packages
这会解析 requirements.txt 文件，并将所有依赖包下载到 packages 目录中。

步骤 2：将下载的包复制到目标机器
使用 USB 驱动器、局域网共享或者其他数据传输方式，将 packages 目录复制到没有网络的目标机器上。

步骤 3：在目标机器上安装依赖包
在目标机器上，打开终端或命令提示符，导航到包含 packages 目录和 requirements.txt 文件的目录，然后运行以下命令：
pip install --no-index --find-links=packages -r requirements.txt



