# -*- encoding=utf8 -*-
__author__ = "zhexin.xiao"

from airtest.core.api import *

from util.check_darkAndlight import darkAndlight
from util.util import get_registered_numberAndid

auto_setup(__file__)


from poco.drivers.ios import iosPoco
poco = iosPoco()
wait(Template(r"tpl1709173565813.png", record_pos=(-0.001, 0.03), resolution=(1125, 2436)))
touch(Template(r"tpl1709173575094.png", record_pos=(0.004, 0.035), resolution=(1125, 2436)))
wait(Template(r"tpl1709173598516.png", record_pos=(-0.217, -0.696), resolution=(1125, 2436)))
touch(Template(r"tpl1709173588026.png", record_pos=(0.046, -0.355), resolution=(1125, 2436)))
dark = Template(r"tpl1709173855578.png", record_pos=(-0.003, 0.032), resolution=(1125, 2436))
number,id = get_registered_numberAndid()
text(number)
light = Template(r"tpl1709173893412.png", record_pos=(-0.0, 0.033), resolution=(1125, 2436))
result = darkAndlight(dark,light)
assert_equal(True,result,'continue按钮点亮验证')
touch(Template(r"tpl1709173757208.png", record_pos=(-0.001, 0.031), resolution=(1125, 2436)))
wait(Template(r"tpl1709180367437.png", record_pos=(-0.256, -0.69), resolution=(1125, 2436)))
text('0000')
touch(Template(r"tpl1709173930146.png", record_pos=(-0.28, 0.305), resolution=(1125, 2436)))
touch(Template(r"tpl1709173932034.png", record_pos=(-0.274, 0.51), resolution=(1125, 2436)))
touch(Template(r"tpl1709173933995.png", record_pos=(-0.277, 0.689), resolution=(1125, 2436)))
touch(Template(r"tpl1709173937554.png", record_pos=(0.002, 0.318), resolution=(1125, 2436)))
touch(Template(r"tpl1709173938807.png", record_pos=(-0.0, 0.502), resolution=(1125, 2436)))
touch(Template(r"tpl1709173942825.png", record_pos=(0.002, 0.694), resolution=(1125, 2436)))
wait(Template(r"tpl1709174034273.png", record_pos=(-0.001, -0.649), resolution=(1125, 2436)))
poco("Great news!").get_name()
poco("You’ve completed 50% of your profile.").get_name()
poco("Complete the next 50% to start using Tiqmo services").get_name()
touch(Template(r"tpl1709180924986.png", record_pos=(-0.004, -0.57), resolution=(1125, 2436)))
wait(Template(r"tpl1709174416595.png", record_pos=(-0.151, -0.892), resolution=(1125, 2436)))
poco("To protect your account and unlock full Tiqmo features, please verify your identity.").get_name()
poco("Province").get_name()
poco("City").get_name()
poco("Address").get_name()
poco("Employer Name (Optional)").get_name()
poco("Employment sector").get_name()
poco("Profession").get_name()
poco("Main Source of Fund").get_name()
poco("Monthly Income").get_name()
touch(Template(r"tpl1709174854971.png", record_pos=(-0.309, -0.479), resolution=(1125, 2436)))
wait(Template(r"tpl1709174891021.png", record_pos=(-0.001, -0.263), resolution=(1125, 2436)))
touch(Template(r"tpl1709174898851.png", record_pos=(-0.003, -0.261), resolution=(1125, 2436)))
touch(Template(r"tpl1709174909520.png", record_pos=(0.073, -0.473), resolution=(1125, 2436)))
wait(Template(r"tpl1709174917705.png", record_pos=(-0.001, -0.259), resolution=(1125, 2436)))
touch(Template(r"tpl1709174930309.png", record_pos=(0.001, -0.259), resolution=(1125, 2436)))
touch(Template(r"tpl1709174938327.png", record_pos=(-0.318, -0.276), resolution=(1125, 2436)))
text('26F ZhongkeDasha')
touch(Template(r"tpl1709174978549.png", record_pos=(-0.145, -0.076), resolution=(1125, 2436)))
text('QA')
touch(Template(r"tpl1709175005542.png", record_pos=(-0.2, 0.123), resolution=(1125, 2436)))
wait(Template(r"tpl1709175024907.png", record_pos=(0.002, -0.104), resolution=(1125, 2436)))
touch(Template(r"tpl1709175024907.png", record_pos=(0.002, -0.104), resolution=(1125, 2436)))
touch(Template(r"tpl1709175057859.png", record_pos=(-0.296, 0.33), resolution=(1125, 2436)))
wait(Template(r"tpl1709177346948.png", record_pos=(-0.007, -0.474), resolution=(1125, 2436)))
touch(Template(r"tpl1709177367578.png", record_pos=(0.002, -0.472), resolution=(1125, 2436)))
touch(Template(r"tpl1709177379425.png", record_pos=(-0.202, 0.522), resolution=(1125, 2436)))
wait(Template(r"tpl1709177389142.png", record_pos=(0.002, -0.101), resolution=(1125, 2436)))
touch(Template(r"tpl1709177394054.png", record_pos=(-0.003, -0.104), resolution=(1125, 2436)))
swipe(Template(r"tpl1709177457421.png", record_pos=(-0.294, 0.647), resolution=(1125, 2436)), vector=[-0.0508, -0.1])
dark = Template(r"tpl1709178026443.png", record_pos=(-0.0, 0.831), resolution=(1125, 2436))
sleep(1)
touch(Template(r"tpl1709177402729.png", record_pos=(-0.241, 0.72), resolution=(1125, 2436)))
wait(Template(r"tpl1709177410619.png", record_pos=(0.007, -0.108), resolution=(1125, 2436)))
touch(Template(r"tpl1709177417375.png", record_pos=(0.005, -0.106), resolution=(1125, 2436)))
light = Template(r"tpl1709178063834.png", record_pos=(-0.001, 0.831), resolution=(1125, 2436))
result = darkAndlight(dark,light)
assert_equal(True,result,'verify identify按钮点亮验证')
poco("Are you the ultimate beneficial owner of the account?").get_name()
poco("Are you or any of your relatives politically exposed person?").get_name()
elements = (poco('signBox')[0].attr('value'),poco('signBox')[3].attr('value'))
assert_equal(('1','1'), elements, "默认点亮问题1的yes和问题2的no")
touch(Template(r"tpl1709178077304.png", record_pos=(-0.001, 0.83), resolution=(1125, 2436)))
wait(Template(r"tpl1709179671688.png", record_pos=(-0.206, 0.404), resolution=(1125, 2436)))
touch(Template(r"tpl1709179677107.png", record_pos=(-0.006, 0.935), resolution=(1125, 2436)))
assert_exists(Template(r"tpl1709179694723.png", record_pos=(-0.002, -0.649), resolution=(1125, 2436)), "主页kyc入口消失")


