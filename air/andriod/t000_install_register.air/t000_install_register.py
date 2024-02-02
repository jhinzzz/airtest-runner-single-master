# -*- encoding=utf8 -*-
__author__ = "zhexin.xiao"

from airtest.core.api import *
from conf.settings import package_name
from util.util import update_next_register_numberAndid, get_next_register_numberAndid, update_registered_numberAndid, \
    enter_opt_page
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
# clear_app(package_name)
# start_app(package_name)
text('') # 设置输入法 默认为yosemite输入法
# wait(Template(r"tpl1706068332333.png", record_pos=(-0.004, -0.236), resolution=(1080, 2340)))
# touch(Template(r"tpl1706068341469.png", record_pos=(-0.002, 0.191), resolution=(1080, 2340)))
wait(Template(r"tpl1706068353035.png", record_pos=(-0.006, 0.008), resolution=(1080, 2340)))
touch(Template(r"tpl1706068364133.png", record_pos=(-0.001, 0.279), resolution=(1080, 2340)))
wait(Template(r"tpl1706068385372.png", record_pos=(0.374, -0.831), resolution=(1080, 2340)))
touch(Template(r"tpl1706068385372.png", record_pos=(0.374, -0.831), resolution=(1080, 2340)))
# wait(Template(r"tpl1706068396736.png", record_pos=(-0.003, -0.117), resolution=(1080, 2340)))
# touch(Template(r"tpl1706068405563.png", record_pos=(-0.006, 0.113), resolution=(1080, 2340)))
# wait(Template(r"tpl1706068414330.png", record_pos=(0.004, 0.019), resolution=(1080, 2340)))
# touch(Template(r"tpl1706068424616.png", record_pos=(-0.004, 0.269), resolution=(1080, 2340)))
wait(Template(r"tpl1706068431017.png", record_pos=(0.016, -0.399), resolution=(1080, 2340)))
touch(Template(r"tpl1706068437644.png", record_pos=(0.159, -0.351), resolution=(1080, 2340)))
number, id = get_next_register_numberAndid()
sleep(1)
text(number)
wait(Template(r"tpl1706068490384.png", record_pos=(0.001, 0.083), resolution=(1080, 2340)))
touch(Template(r"tpl1706068496146.png", record_pos=(-0.004, 0.083), resolution=(1080, 2340)))
wait(Template(r"tpl1706068503730.png", record_pos=(-0.009, -0.397), resolution=(1080, 2340)))
touch(Template(r"tpl1706068512006.png", record_pos=(-0.145, -0.368), resolution=(1080, 2340)))
text(id)
wait(Template(r"tpl1706068546013.png", record_pos=(-0.004, 0.069), resolution=(1080, 2340)))
touch(Template(r"tpl1706068557530.png", record_pos=(-0.001, 0.062), resolution=(1080, 2340)))
wait(Template(r"tpl1706499557082.png", record_pos=(-0.002, -0.794), resolution=(1080, 2340)))
enter_opt_page()
wait(Template(r"tpl1706068594676.png", record_pos=(-0.006, -0.317), resolution=(1080, 2340)))
touch(Template(r"tpl1706068602624.png", record_pos=(-0.001, 0.213), resolution=(1080, 2340)))
wait(Template(r"tpl1706068610738.png", record_pos=(-0.016, -0.37), resolution=(1080, 2340)))
sleep(9)
wait(Template(r"tpl1706068629656.png", record_pos=(0.001, -0.104), resolution=(1080, 2340)))
touch(Template(r"tpl1706068636582.png", record_pos=(-0.258, 0.03), resolution=(1080, 2340)))
touch(Template(r"tpl1706068638796.png", record_pos=(-0.258, 0.232), resolution=(1080, 2340)))
touch(Template(r"tpl1706068640636.png", record_pos=(-0.27, 0.418), resolution=(1080, 2340)))
touch(Template(r"tpl1706068645351.png", record_pos=(0.007, 0.039), resolution=(1080, 2340)))
touch(Template(r"tpl1706068646120.png", record_pos=(-0.002, 0.218), resolution=(1080, 2340)))
touch(Template(r"tpl1706068647230.png", record_pos=(0.001, 0.432), resolution=(1080, 2340)))
wait(Template(r"tpl1706068655190.png", record_pos=(-0.003, -0.09), resolution=(1080, 2340)))
touch(Template(r"tpl1706068636582.png", record_pos=(-0.258, 0.03), resolution=(1080, 2340)))
touch(Template(r"tpl1706068638796.png", record_pos=(-0.258, 0.232), resolution=(1080, 2340)))
touch(Template(r"tpl1706068640636.png", record_pos=(-0.27, 0.418), resolution=(1080, 2340)))
touch(Template(r"tpl1706068645351.png", record_pos=(0.007, 0.039), resolution=(1080, 2340)))
touch(Template(r"tpl1706068646120.png", record_pos=(-0.002, 0.218), resolution=(1080, 2340)))
touch(Template(r"tpl1706068647230.png", record_pos=(0.001, 0.432), resolution=(1080, 2340)))
sleep(2)
wait(Template(r"tpl1706499676656.png", record_pos=(-0.066, -0.865), resolution=(1080, 2340)))
update_next_register_numberAndid(number,id)
update_registered_numberAndid(number,id)
wait(Template(r"tpl1706499684925.png", record_pos=(-0.006, -0.606), resolution=(1080, 2340)))
wait(Template(r"tpl1706068707089.png", record_pos=(0.001, 0.56), resolution=(1080, 2340)))
touch(Template(r"tpl1706068714793.png", record_pos=(0.006, 0.866), resolution=(1080, 2340)))
sleep(2)
wait(Template(r"tpl1706506911530.png", record_pos=(-0.078, -0.86), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1706506935099.png", record_pos=(-0.001, -0.592), resolution=(1080, 2340)), "home page上半部分校验")
assert_exists(Template(r"tpl1706506956315.png", record_pos=(-0.001, 0.038), resolution=(1080, 2340)), "home page下半部分校验")

touch(Template(r"tpl1706068778323.png", record_pos=(-0.387, -0.851), resolution=(1080, 2340)))
wait(Template(r"tpl1706068806696.png", record_pos=(0.004, 0.028), resolution=(1080, 2340)))
touch(Template(r"tpl1706068815669.png", record_pos=(-0.01, 0.191), resolution=(1080, 2340)))
wait(Template(r"tpl1706604769385.png", record_pos=(-0.224, -0.894), resolution=(1080, 2340)))
text = poco("cn.swiftpass.wallet.tiqmo:id/tv_phone").attr("text")
assert_equal(text, '+966' + number, 'My Profile注册手机号验证[{}]' .format(number))










