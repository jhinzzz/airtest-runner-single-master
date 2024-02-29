# -*- encoding=utf8 -*-
__author__ = "zhexin.xiao"

from airtest.core.api import *

from util.util import get_money_number

auto_setup(__file__)
from poco.drivers.ios import iosPoco
poco = iosPoco()
wait(Template(r"tpl1709173565813.png", record_pos=(-0.001, 0.03), resolution=(1125, 2436)))
touch(Template(r"tpl1709173575094.png", record_pos=(0.004, 0.035), resolution=(1125, 2436)))
wait(Template(r"tpl1709173598516.png", record_pos=(-0.217, -0.696), resolution=(1125, 2436)))
touch(Template(r"tpl1709173588026.png", record_pos=(0.046, -0.355), resolution=(1125, 2436)))
number = get_money_number()
text(number)
touch(Template(r"tpl1709173757208.png", record_pos=(-0.001, 0.031), resolution=(1125, 2436)))
wait(Template(r"tpl1709180367437.png", record_pos=(-0.256, -0.69), resolution=(1125, 2436)))
text('0000')
touch(Template(r"tpl1709173930146.png", record_pos=(-0.28, 0.305), resolution=(1125, 2436)))
touch(Template(r"tpl1709173932034.png", record_pos=(-0.274, 0.51), resolution=(1125, 2436)))
touch(Template(r"tpl1709173933995.png", record_pos=(-0.277, 0.689), resolution=(1125, 2436)))
touch(Template(r"tpl1709173937554.png", record_pos=(0.002, 0.318), resolution=(1125, 2436)))
touch(Template(r"tpl1709173938807.png", record_pos=(-0.0, 0.502), resolution=(1125, 2436)))
touch(Template(r"tpl1709173942825.png", record_pos=(0.002, 0.694), resolution=(1125, 2436)))
wait(Template(r"tpl1709188188746.png", record_pos=(-0.281, -0.567), resolution=(1125, 2436)))
balance = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").offspring(type='StaticText')[2].attr('name')
touch(Template(r"tpl1709188224709.png", record_pos=(-0.277, -0.57), resolution=(1125, 2436)))
wait(Template(r"tpl1709188248414.png", record_pos=(0.001, 0.642), resolution=(1125, 2436)))
touch(Template(r"tpl1709188255622.png", record_pos=(0.001, 0.644), resolution=(1125, 2436)))
wait(Template(r"tpl1709188284168.png", record_pos=(-0.231, 0.007), resolution=(1125, 2436)))
touch(Template(r"tpl1709188293750.png", record_pos=(-0.08, 0.228), resolution=(1125, 2436)))
dark = poco('ADD MONEY').attr('isEnabled')
assert_equal(dark, "0", "add money按钮不可点击.")
amount = '100.01'
text(amount)
light = poco('ADD MONEY').attr('isEnabled')
assert_equal(light, "1", "add money按钮可点击.")
touch(Template(r"tpl1709188631222.png", record_pos=(0.002, 0.196), resolution=(1125, 2436)))
wait(Template(r"tpl1709188647279.png", record_pos=(0.284, 0.013), resolution=(1125, 2436)))
touch(Template(r"tpl1709190288073.png", record_pos=(-0.002, 0.218), resolution=(1125, 2436)))
wait(Template(r"tpl1709193228871.png", record_pos=(-0.001, 0.279), resolution=(1125, 2436)))
count = len(poco('{} SAR' .format(amount)))
assert_equal(count, 2, "校验两个amount金额.")
assert_exists(Template(r"tpl1709190655264.png", record_pos=(-0.001, 0.281), resolution=(1125, 2436)), "图片校验")
assert_equal(poco('CONFIRM').attr('isEnabled'), "1", "Confirm按钮可点击")
touch(Template(r"tpl1709190763216.png", record_pos=(-0.0, 0.916), resolution=(1125, 2436)))
wait(Template(r"tpl1709190789099.png", record_pos=(-0.326, -0.792), resolution=(1125, 2436)))
touch(Template(r"tpl1709190789099.png", record_pos=(-0.326, -0.792), resolution=(1125, 2436)))
touch(Template(r"tpl1709190842810.png", record_pos=(-0.42, -0.898), resolution=(1125, 2436)))
wait(Template(r"tpl1709190883811.png", record_pos=(-0.0, -0.181), resolution=(1125, 2436)))
assert_exists(Template(r"tpl1709190899691.png", record_pos=(-0.003, 0.332), resolution=(1125, 2436)), "充值回执")
touch(Template(r"tpl1709191332112.png", record_pos=(-0.163, -0.879), resolution=(1125, 2436)))
new_balance = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").offspring(type='StaticText')[2].attr('name')
total = float(balance)+float(amount)
est_balance = str('%.2f' % total)
assert_equal(new_balance, est_balance, "总金额校验.")






