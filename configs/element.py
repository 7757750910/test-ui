from selenium.webdriver.common.by import By


class Element:
    # 登录页面----------
    # 下拉箭头
    LOGIN_laxiajiantou = (By.CLASS_NAME, "icon-xiangxiajiantou")
    # 选择租户--中核华辉租户
    LOGIN_xuanzezuhu = (By.CSS_SELECTOR, ".el-dropdown-menu--default li:first-child")
    # 输入账号/输入密码
    LOGIN_shuruzhanghao = (By.CLASS_NAME, "el-input__inner")
    # 登录按钮
    LOGIN_denglu = (By.CLASS_NAME, "login-content-submit")
    # 登录成功信息提示
    LOGIN_dengluxinxi = (By.CLASS_NAME, "el-message__content")

    # 首页---------------应用配置菜单
    HOME_yingyongpeizhi = (By.CSS_SELECTOR, "i.icon-yijicaidan_yingyongpeizhi-fill:first-of-type")

    # 应用配置-引擎管理
    YYPZ_yingqinguanli = (By.CLASS_NAME, "icon-erjicaidan_yinqingguanli-line")

    # 应用配置-引擎管理-表单引擎
    YYPZ_YQGL_biaodanyinqing = (By.CSS_SELECTOR,
                                "#app > section > div > aside > div.el-scrollbar.flex-auto.flex-auto-zhlx > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul > li.el-sub-menu.is-opened.zhlx-vertical-submenu > ul > div > div:nth-child(1) > li > ul > div > div:nth-child(1) > li > div > span")

    # 应用配置-引擎管理-表单引擎-表单设计器
    YYPZ_YQGL_BDYQ_biaodanshejiqi = (By.CSS_SELECTOR,
                                     "#app > section > div > aside > div.el-scrollbar.flex-auto.flex-auto-zhlx > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > ul > li.el-sub-menu.is-opened.zhlx-vertical-submenu > ul > div > div:nth-child(1) > li > ul > div > div:nth-child(1) > li > ul > div > div:nth-child(1) > li > span")

    # 应用配置-引擎管理-表单引擎-表单设计器_新增按钮 ---》跳转到 表单设计--基础信息页面
    YYPZ_YQGL_BDYQ_BDSJQ_add = (By.CSS_SELECTOR,
                                "#app > section > section > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > main > div.el-scrollbar.layout-main-scroll.layout-backtop-header-fixed > div.layout-main-scroll.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > div:nth-child(1) > div.layout-padding-auto.layout-padding-view > form > div > div.visi-btn-group > button:nth-child(1) > span")

    # 表单设计页面--基础信息 ---》表单名称输入框
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_mingcheng = (By.CSS_SELECTOR, ".el-input__inner[placeholder='表单名称']")

    # 表单设计页面--基础信息 ---》分类
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_fenlei = (By.CSS_SELECTOR,
                                        "div.el-row.is-justify-center.is-align-middle.basic-box > div > form > div:nth-child(4) > div > div > div > div.el-select__selection > div.el-select__selected-item.el-select__placeholder.is-transparent")

    # 表单设计页面--基础信息 ---》分类--选择分类
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_FL_xuanze = (By.CSS_SELECTOR, ".el-select-dropdown__list li:first-child")

    # 表单设计页面--基础信息 ---》表单说明输入框
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_biaodanshuoming = (By.CSS_SELECTOR, ".el-textarea__inner[placeholder='流程说明']")

    # 表单设计页面--基础信息 ---》下一步按钮
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_xiayibu = (By.CSS_SELECTOR,
                                         "#app > section > section > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > main > div.el-scrollbar.layout-main-scroll.layout-backtop-header-fixed > div.layout-main-scroll.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > div:nth-child(1) > div:nth-child(2) > div > div > header > div > div.el-scrollbar > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > button:nth-child(2)")

    # 表单设计页面--表单设计页面-左右布局
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_zuoyoubuju = (By.CSS_SELECTOR, ".container-widget-item[title='左右布局']")

    # 表单设计页面--表单设计页面-视图
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_shitu = (By.CSS_SELECTOR,
                                            "div.layout-padding > div.layout-padding-auto.layout-padding-view > div > section > section > section > main > div.el-scrollbar.container-scroll-bar > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > form")

    # 表单设计页面--表单设计页面-保存按钮
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocun = (By.CSS_SELECTOR,
                                             "#app > section > section > div > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > main > div.el-scrollbar.layout-main-scroll.layout-backtop-header-fixed > div.layout-main-scroll.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > div:nth-child(1) > div:nth-child(2) > div > div > header > div > div.el-scrollbar > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > div > button.el-button.el-button--primary.el-button--default")

    # 表单设计页面--表单设计页面-保存成功信息提示
    YYPZ_YQGL_BDYQ_BDSJQ_BDSJ_BDSJ_baocunchenggong = (By.CLASS_NAME, "el-message__content")
