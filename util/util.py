import os
import configparser
from conf.settings import env
import requests
from bs4 import BeautifulSoup
curpath = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(curpath + '/conf/', 'data.ini')
env = env

def conf_act(method, content, path=path):
    conf = configparser.ConfigParser()  # 类的实例化
    conf.read(path, encoding="utf-8")
    if method == 'items':
        value = conf.items(content)
        return value
    elif method == 'get':
        item = content.split('|')[0]
        key = content.split('|')[1]
        value = conf.get(item, key)
        return value
    elif method == 'set':
        section = content.split('|')[0]
        item = content.split('|')[1]
        key = content.split('|')[2]
        print(section, item, key)
        conf.set(section, item, key)
        conf.write(open(path, "w"))


def get_next_register_numberAndid():
    number = conf_act('get', '{}|next_register_phone'.format(env))
    id = conf_act('get', '{}|next_register_id'.format(env))
    return number, id


def update_next_register_numberAndid(used_number, used_id):
    new_number = int(used_number) + 1
    conf_act('set', '{}|next_register_phone|{}'.format(env, new_number))
    new_id = int(used_id) + 1
    conf_act('set', '{}|next_register_id|{}'.format(env, new_id))


def update_registered_numberAndid(number, id):
    conf_act('set', '{}|registered_phone|{}'.format(env, number))
    conf_act('set', '{}|registered_id|{}'.format(env, id))


def get_registered_numberAndid():
    number = conf_act('get', '{}|registered_phone'.format(env))
    id = conf_act('get', '{}|registered_id'.format(env))
    return number, id


def update_kyced_numberAndid(number, id):
    conf_act('set', '{}|kyced_phone|{}'.format(env, number))
    conf_act('set', '{}|kyced_id|{}'.format(env, id))


def get_ref_link():
    value = conf_act('get', '{}|ref_link'.format(env))
    return value


def get_kyced_numberAndid():
    number = conf_act('get', '{}|kyced_phone'.format(env))
    id = conf_act('get', '{}|kyced_id'.format(env))
    return number, id

def get_andriod_permissions():
    permissions = conf_act('get', 'andriod_permission|permission')
    return permissions.split(',')

def air_device_dir(device, air_dir):
    if 'android' in device:
        air_dir = os.path.join(air_dir, 'andriod')
        return air_dir, 'android'
    elif 'iOS' in device:
        air_dir = os.path.join(air_dir, 'ios')
        return air_dir, 'iOS'

def define_device_type(dev_id):
    if 'android' in dev_id:
        return 'android'
    elif 'iOS' in dev_id:
        return 'iOS'

# 输入opt
def enter_opt_page():
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    for i in range(4):
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring(
            "cn.swiftpass.wallet.tiqmo:id/verift_otp").child("android.widget.EditText")[i].set_text('0')

if __name__ == '__main__':
    print(get_registered_numberAndid())
