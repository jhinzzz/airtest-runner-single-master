# -*- encoding=utf8 -*-
__author__ = "zhexin.xiao"
from airtest.core.api import *
from util.check_darkAndlight import darkAndlight
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from util.util import get_kyced_numberAndid, enter_opt_page

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)
wait(Template(r"tpl1706594530160.png", record_pos=(-0.001, 0.004), resolution=(1080, 2340)))
touch(Template(r"tpl1706594541921.png", record_pos=(-0.006, 0.284), resolution=(1080, 2340)))
wait(Template(r"tpl1706068385372.png", record_pos=(0.374, -0.831), resolution=(1080, 2340)))
touch(Template(r"tpl1706068385372.png", record_pos=(0.374, -0.831), resolution=(1080, 2340)))
wait(Template(r"tpl1706604561687.png", record_pos=(-0.208, -0.659), resolution=(1080, 2340)))
dark = (Template(r"tpl1706596410914.png", record_pos=(0.001, 0.081), resolution=(1080, 2340)))
touch(Template(r"tpl1706594567489.png", record_pos=(0.155, -0.344), resolution=(1080, 2340)))
number,id = get_kyced_numberAndid()
text(number)
light = Template(r"tpl1706598367507.png", record_pos=(-0.002, 0.083), resolution=(1080, 2340))
result = darkAndlight(light,dark)
assert_equal(True, result, "输入手机号 按钮点亮 断言成功.")
touch(Template(r"tpl1706600530194.png", record_pos=(-0.001, 0.081), resolution=(1080, 2340)))
wait(Template(r"tpl1706604358749.png", record_pos=(-0.251, -0.685), resolution=(1080, 2340)))
enter_opt_page()
touch(Template(r"tpl1706587327007.png", record_pos=(-0.004, -0.624), resolution=(1080, 2340)))
wait(Template(r"tpl1706600613432.png", record_pos=(-0.001, -0.139), resolution=(1080, 2340)))
touch(Template(r"tpl1706600631517.png", record_pos=(-0.256, 0.015), resolution=(1080, 2340)))
touch(Template(r"tpl1706600633913.png", record_pos=(-0.253, 0.208), resolution=(1080, 2340)))
touch(Template(r"tpl1706600635175.png", record_pos=(-0.262, 0.4), resolution=(1080, 2340)))
touch(Template(r"tpl1706600637694.png", record_pos=(0.004, 0.02), resolution=(1080, 2340)))
touch(Template(r"tpl1706600638572.png", record_pos=(0.01, 0.2), resolution=(1080, 2340)))
touch(Template(r"tpl1706600640605.png", record_pos=(0.004, 0.4), resolution=(1080, 2340)))
sleep(2.5)
wait(Template(r"tpl1706605681731.png", record_pos=(-0.045, -0.852), resolution=(1080, 2340)))
balance = poco("cn.swiftpass.wallet.tiqmo:id/tv_amount").attr('text')
touch(Template(r"tpl1706600678722.png", record_pos=(-0.305, -0.216), resolution=(1080, 2340)))
wait(Template(r"tpl1706600704302.png", record_pos=(0.001, 0.592), resolution=(1080, 2340)))
touch(Template(r"tpl1706600722940.png", record_pos=(-0.001, 0.557), resolution=(1080, 2340)))
wait(Template(r"tpl1706601406883.png", record_pos=(-0.231, 0.022), resolution=(1080, 2340)))
dark = Template(r"tpl1706600785830.png", record_pos=(-0.003, 0.912), resolution=(1080, 2340))
touch(Template(r"tpl1706602042641.png", record_pos=(-0.007, 0.251), resolution=(1080, 2340)))
amount = '100.00'
text(amount)
light = Template(r"tpl1706600803926.png", record_pos=(-0.004, 0.906), resolution=(1080, 2340))
result = darkAndlight(light,dark)
assert_equal(True, result, "Add Money 按钮点亮 断言成功.")
touch(Template(r"tpl1706606403576.png", record_pos=(-0.001, 0.908), resolution=(1080, 2340)))
wait(Template(r"tpl1706606162756.png", record_pos=(0.261, 0.145), resolution=(1080, 2340)))
touch(Template(r"tpl1706606170899.png", record_pos=(0.257, 0.145), resolution=(1080, 2340)))
wait(Template(r"tpl1706600868107.png", record_pos=(-0.002, -0.302), resolution=(1080, 2340)))
touch(Template(r"tpl1706600875668.png", record_pos=(-0.226, -0.344), resolution=(1080, 2340)))
text('4111111111111111')
touch(Template(r"tpl1706600981924.png", record_pos=(-0.14, -0.16), resolution=(1080, 2340)))
wait(Template(r"tpl1706686556098.png", record_pos=(0.337, 0.358), resolution=(1080, 2340)))
swipe(Template(r"tpl1706601012620.png", record_pos=(-0.237, 0.803), resolution=(1080, 2340)), vector=[0.003, -0.1819])
touch(Template(r"tpl1706601036703.png", record_pos=(0.328, 0.359), resolution=(1080, 2340)))
touch(Template(r"tpl1706601048566.png", record_pos=(0.275, -0.133), resolution=(1080, 2340)))
text('123')
dark = Template(r"tpl1706601148501.png", record_pos=(0.001, 0.288), resolution=(1080, 2340))
text('automatic test name')
light = Template(r"tpl1706601173273.png", record_pos=(-0.006, 0.286), resolution=(1080, 2340))
result = darkAndlight(light,dark)
assert_equal(True, result, "Add New Card 按钮点亮 断言成功.")
touch(Template(r"tpl1706601213607.png", record_pos=(0.001, 0.288), resolution=(1080, 2340)))
wait(Template(r"tpl1706601489866.png", record_pos=(-0.101, 0.098), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1706601275873.png", record_pos=(-0.004, 0.495), resolution=(1080, 2340)), "confirm transaction 断言")
touch(Template(r"tpl1706601295906.png", record_pos=(-0.001, 0.918), resolution=(1080, 2340)))
wait(Template(r"tpl1706601518286.png", record_pos=(-0.317, -0.763), resolution=(1080, 2340)))
touch(Template(r"tpl1706601315643.png", record_pos=(-0.324, -0.785), resolution=(1080, 2340)))
wait(Template(r"tpl1706601540803.png", record_pos=(-0.101, -0.063), resolution=(1080, 2340)))
assert_exists(Template(r"tpl1706607502139.png", record_pos=(0.0, -0.039), resolution=(1080, 2340)), "充值100 断言")
touch(Template(r"tpl1706601632032.png", record_pos=(0.006, -0.853), resolution=(1080, 2340)))
wait(Template(r"tpl1706601652086.png", record_pos=(0.199, 0.931), resolution=(1080, 2340)))
touch(Template(r"tpl1706601658024.png", record_pos=(0.202, 0.937), resolution=(1080, 2340)))
wait(Template(r"tpl1706602911815.png", record_pos=(-0.216, -0.894), resolution=(1080, 2340)))
amount_earn=poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("cn.swiftpass.wallet.tiqmo:id/main_container").offspring("cn.swiftpass.wallet.tiqmo:id/vp_history_main").offspring("cn.swiftpass.wallet.tiqmo:id/sw_history").offspring("cn.swiftpass.wallet.tiqmo:id/ry_transaction_history").child("android.view.ViewGroup")[0].offspring("android.view.ViewGroup").child("android.widget.LinearLayout").offspring("cn.swiftpass.wallet.tiqmo:id/tv_money").attr("text")
assert_equal('+ {} SAR' .format(amount), amount_earn, "历史充值金额校验")
touch(Template(r"tpl1706602677800.png", record_pos=(-0.001, 0.931), resolution=(1080, 2340)))
wait(Template(r"tpl1706604997831.png", record_pos=(-0.059, -0.853), resolution=(1080, 2340)))
new_balance = poco("cn.swiftpass.wallet.tiqmo:id/tv_amount").attr('text')
assert_equal(float(new_balance), float(balance)+float(amount), "主页金额balance 断言.")



