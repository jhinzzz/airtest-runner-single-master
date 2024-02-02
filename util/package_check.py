import os
import zipfile, plistlib, sys, re
from log.log import logger

def analyze_ipa_with_plistlib(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    ipa_file.close()
    logger.info('IOS本地包[地址: %s]' % ipa_path)
    logger.info('本地包检查结果: Display Name: [%s]; Bundle Identifier: [%s]; Version: [%s]' % (
        plist_root['CFBundleName'], plist_root['CFBundleIdentifier'], plist_root['CFBundleVersion']))

def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

def find_package(loc, type):
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_package_path = os.path.join(root_path, loc)
    for root, dirs, files in os.walk(app_package_path):
        if any(file.endswith(".%s" % type) for file in files):
            for file in files:
                if file.endswith(".%s" % type):
                    file_path = os.path.join(root, file)
                    logger.info('检测安装包存在 [%s]' % file_path)
                    return file_path
        else:
            logger.info("[%s] 目录下不存在 %s文件，请确保%s文件在该目录下" % (app_package_path, type,type))
            raise SystemExit

if __name__ == '__main__':
    find_package('app_package','apk')