#!/usr/python3
# author:zhexin xiao
import logging
import re
import shutil, jinja2, datetime
import unittest
import concurrent.futures
from airtest.utils.apkparser import APK
from argparse import *
from conf.settings import *
from airtest.report.report import LogToHtml
from airtest.cli.runner import AirtestCase, run_script

from util.package_check import find_package, analyze_ipa_with_plistlib
from util.send_email import EmailSender
from util.subp import *
from util.util import air_device_dir, get_andriod_permissions, define_device_type, findDeviceName
from log.log import logger
from airtest.core.api import *
import subprocess

class Air_Case_Handler(AirtestCase):
    def __init__(self, dev_id):
        super(Air_Case_Handler, self).__init__()
        if deviceType.upper() == "WEB":
            pass
        else:
            # 如果deviceType非“Web”，则为app
            # 连接安卓app，实现自动化检查版本和安装
            self.connect_check_package(dev_id)

    def setUp(self):
        super(Air_Case_Handler, self).setUp()

    def tearDown(self):
        super(Air_Case_Handler, self).tearDown()

    def run_air(self, air_dir, device):
        # 判断设备定义 设备的用例地址 device_type如果是安卓则用例库air_dir为air下的andriod文档
        air_dir, device_type = air_device_dir(device=device, air_dir=air_dir)
        start_time = datetime.datetime.now()
        start_time_fmt = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        results = []  # {name:项目名，result:运行结果True/False}
        root_log = log_path
        if device_type == "andriod":
            device_name = str(re.search(r'///(.+):', device).group(1))
        elif device_type == 'iOS':
            device_name = findDeviceName(device)
        self.log_report_file_exist(log_path)
        air_files = os.listdir(air_dir)
        logger.info('------- Start Testing %s  -------' % device_name)
        # 读取执行用例文件并执行用例
        for file in air_files:
            # 找到air目录下所有后缀是.air的脚本
            if file.endswith(".air"):
                airName = file
                # 把文件路径的后缀删掉，就变成了文件路径了。后面用来做脚本同名的log日志文件夹
                airDirName = file.replace(".air",
                                          "")
                script = os.path.join(air_dir,
                                      file)
                # log的路径
                air_log = os.path.join(root_log, airDirName + device_name + '_' + str(datetime.datetime.now().strftime(
                    "%Y%m%d%H%M")))
                # 创建log的目录
                os.makedirs(air_log)
                html = os.path.join(air_log, "log.html")
                if deviceType.upper() == "WEB":
                    # 直接向argparse的namespace添加命令行参数
                    args = Namespace(device=None, log=air_log, recording=None, script=script, compress=compress,
                                     no_image=no_image, language="zh")
                elif deviceType.upper() == "APP":
                    args = Namespace(device=device, log=air_log, recording=None, script=script, language="zh",
                                     compress=compress, no_image=no_image)
                else:
                    args = Namespace(device=device, log=air_log, recording=None, script=script,
                                     language="zh")
                self.clear_dataAndgrant_permissionAndkill_all_service(device_type)
                if device_type == 'andriod':
                    package_name = andriod_package_name
                elif device_type == 'iOS':
                    package_name = ios_package_name
                self.dev.start_app(package_name)

                try:
                    logger.info('------- Total Testing Cases:[%s] Start Case: [%s] -------' % (
                        len(air_files), air_files.index(file) + 1))
                    run_script(args)
                    logger.info('------- Total Testing Cases:[%s] End Case: [%s] -------' % (
                        len(air_files), air_files.index(file) + 1))

                except AssertionError as e:
                    pass

                finally:
                    if deviceType.upper() == "WEB":
                        rpt = LogToHtml(script, air_log, plugins=["airtest_selenium.report"])
                    else:
                        rpt = LogToHtml(script, air_log)
                    rpt.report(output_file=html)
                    result = {}
                    result["name"] = airName.replace('.air', '')
                    result["result"] = rpt.test_result
                    result["log_air"] = air_log
                    results.append(result)
                    self.dev.stop_app(package_name)
                    logger.info('------- End testing %s -------' % device_type)

        end_time = datetime.datetime.now()
        end_time_fmt = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        duration = (end_time - start_time).seconds

        # 创建一个文件系统加载器对象
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            extensions=(),
            autoescape=True
        )
        # 获取一个模板文件
        template = env.get_template(template_name, template_path)
        project_name = root_path.split("/")[-1]
        success = 0
        fail = 0

        # 根据results的值，统计success和fail的总数
        for res in results:
            if res['result']:
                success += 1
            else:
                fail += 1
        report_name = "report_" + device_name + "_" + end_time.strftime("%Y%m%d%H%M") + ".html"
        # 渲染
        html = template.render(
            {"results": results, "device": device, "stime": start_time_fmt, 'etime': end_time_fmt, 'duration': duration,
             "project": project_name, "success": success, "fail": fail})
        # 把渲染后的html写到指定的报告中
        output_file = os.path.join(root_path, "report", report_name)
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)
        EmailSender('执行结束通知', '总计数量：{}，成功：{}，失败：{}' .format(len(results), success, fail)).send_email()

    # airtest日志和报告清理
    def log_report_file_exist(self, log_path):
        root_log = log_path
        # 如果没有log和report目录则创建，有则删除后再创建
        if devices.index(device) == 0:
            if os.path.exists(root_log):
                if cover_air_log:
                    logger.info('------- 清理脚本log日志 -------')
                    shutil.rmtree(root_log)
                    os.makedirs(root_log)
            else:
                os.makedirs(root_log)
            if os.path.exists(report_path):
                if cover_report:
                    logger.info('------- 清理report报告 -------')
                    shutil.rmtree(report_path)
                    os.makedirs(report_path)
            else:
                os.makedirs(report_path)

    # 检查是否有安装包，有则判断版本，没有则安装，版本不符合则安装本地包
    def connect_check_package(self, dev_id):
        device_type = define_device_type(dev_id)
        if device_type == 'iOS':
            connect_wda()
        self.dev = connect_device(dev_id)
        if device_type == 'andriod':
            # 检查是否有安装包
            try:
                if self.dev.check_app(andriod_package_name):
                    # 检查手机包的版本号
                    app_version = \
                        self.dev.adb.shell("dumpsys package {} | grep versionName".format(andriod_package_name)).split('=')[
                            1].strip()
                    if app_version == version_code:
                        logger.info('版本号检查通过current version:{}'.format(version_code))
                    else:
                        logger.info('手机测试包不合格，卸载当前app并安装本地包')
                        self.dev.uninstall_app(andriod_package_name)
                        self.check_install_local_package(device_type)
            # 没有则安装
            except:
                logger.info('手机未安装测试包，检查本地包是否符合要求')
                self.check_install_local_package(device_type)
            try:
                if self.dev.check_app('com.netease.nie.yosemite'):
                    pass
            except:
                logger.info('yosemite apk不存在')
                yosemite_package_loc = find_package('related_app', 'apk')
                self.dev.install_app(filepath=yosemite_package_loc,install_options=['-t','-d','-g'])
        elif device_type == 'iOS':
            app_version = output_app_version()
            if app_version == version_code:
                logger.info('版本号检查通过current version:{}'.format(version_code))
            else:
                logger.info('手机测试包不合格，卸载当前app并安装本地包')
                ios_uninstall(ios_package_name)
                self.check_install_local_package(device_type)


    # 检查本地包是否符合版本，符合则安装，不符合退出
    def check_install_local_package(self,device_type):
        if device_type == 'andriod':
            andriod_package_loc = find_package('app_package','apk')
            apk_version = APK(andriod_package_loc).androidversion_name
            # 准备安装本地包，检查本地包版本
            if apk_version == version_code:
                logger.info('本地包版本号检查通过 {}'.format(apk_version))
                self.dev.install_app(filepath=andriod_package_loc,install_options=['-t','-d','-g'])
            else:
                logger.info('本地包版本号检查不通过，强制退出运行，请更新安装包版本:{}，现测试版本号：{}'.format(apk_version,
                                                                                                             version_code))
                raise SystemExit
        elif device_type == 'iOS':
            ios_package_loc = find_package('app_package','ipa')
            ipa_version = analyze_ipa_with_plistlib(ios_package_loc)
            if ipa_version == version_code:
                logger.info('本地包版本号检查通过 {}'.format(ipa_version))
                ios_install(ios_package_loc)
            else:
                logger.info('本地包版本号检查不通过，强制退出运行，请更新安装包版本:{}，现测试版本号：{}'.format(ipa_version,
                                                                                                             version_code))
                raise SystemExit

    def clear_dataAndgrant_permissionAndkill_all_service(self, device_type):
        """
        安卓清理app缓存，并赋予授权。
        :param device_type:
        :return:
        """
        if device_type == 'andriod':
            # 清理app数据，保持全新安装状态
            self.dev.adb.shell('pm clear {}'.format(andriod_package_name))
            # 清理安卓后台应用
            self.dev.adb.shell('am kill-all')
            permissions_list = get_andriod_permissions()
            for permission in permissions_list:
                try:
                    self.dev.adb.shell('pm grant {} android.permission.{}'.format(andriod_package_name, permission))
                except:
                    pass
        else:
            pass




if __name__ == "__main__":
    for device in devices:
        logger.info('------- 设备[%s]开始执行 -------' % device)
        test = Air_Case_Handler(device)
        test.run_air(air_path, device)
        logger.info('------- 设备[%s]结束执行 -------' % device)

