# coding = utf-8
# author:zhexin xiao
import os
from airtest.core.settings import Settings as ST
# 测试环境 SIT/UAT
env = 'UAT'
# 设备信息，只有当deviceType为app是有效
devices = ['iOS:///http+usbmux://00008101-000961122651003A:8100']
# app名称
andriod_package_name = 'cn.swiftpass.wallet.tiqmo'
ios_package_name = 'com.tiqmo.wallet.ksa.uat'
# download_url
download_url = "https://hw.hstytest.com/tiqmo/appdownload/tiqmo_wallet/uat/aos/download.html?/home/kite_wft/apphome/saasWallyt2/appDownload/tiqmo_wallet/qrInfo.txt"
# app版本号
version_code = '2.2.0'
# 设备类别：app、win和web
deviceType = "app"
# 测试报告模板名称
template_name = "summary_template.html"
# 是否覆盖测试报告,True:运行时会删除之前所有的报告。False：不会删除
cover_report = False
# 是否覆盖脚本日志,True:运行时会删除之前所有的脚本log记录。False：不会删除
cover_air_log = True
# 是否要截图
no_image = False
# 截图压缩精度 1-99 越大越清晰
compress = 99
# 工程根目录
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 脚本目录
air_path = os.path.join(root_path, 'air')
# 日志目录
log_path = os.path.join(root_path, 'log\\air_log')
# 系统执行日志
system_log_path = os.path.join(root_path, 'log\\SystemLog')
# 测试报告模板目录
template_path = os.path.join(root_path, 'template')
# 测试报告路径
report_path = os.path.join(root_path, 'report')
# 测试数据目录
data_path = os.path.join(root_path, 'data')
# airtest 配置(定义airtest库的setting为ST)
ST.THRESHOLD = 0.85  # 识别阈值
ST.THRESHOLD_STRICT = 0.95  # 断言阈值
ST.OPDELAY = 0.1  # 操作间隔
ST.FIND_TIMEOUT = 8  # 查找超时 touch, double_click, swipe, wait, assert_exists
ST.FIND_TIMEOUT_TMP = 3  # swipe,exists,assert_not_exists
# ST.CVSTRATEGY = ["mstpl", "tpl", "sift", "surf", "kaze", "akaze", "brisk"]
# CVSTRATEGY = ["mstpl", "tpl", "surf", "brisk"]