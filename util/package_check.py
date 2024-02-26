import os
import zipfile, plistlib, sys, re


def analyze_ipa_with_plistlib(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    ipa_file.close()
    print('IOS本地包[地址: %s]' % ipa_path)
    print('本地包检查结果: Display Name: [%s]; Bundle Identifier: [%s]; Version: [%s]' % (
        plist_root['CFBundleName'], plist_root['CFBundleIdentifier'], plist_root['CFBundleShortVersionString']))
    return plist_root['CFBundleShortVersionString']
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
                    print('检测安装包存在 [%s]' % file_path)
                    return file_path
        else:
            print("[%s] 目录下不存在 %s文件，请确保%s文件在该目录下" % (app_package_path, type,type))
            raise SystemExit

if __name__ == '__main__':
    ios_loc = find_package('app_package','ipa')
    analyze_ipa_with_plistlib(ios_loc)