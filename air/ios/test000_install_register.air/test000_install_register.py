# -*- encoding=utf8 -*-
__author__ = "zhexin.xiao"

from airtest.core.api import *

from conf.settings import ios_package_name
from util.package_check import find_package
from util.subp import ios_uninstall, ios_install
from util.util import update_next_register_numberAndid, get_next_register_numberAndid, update_registered_numberAndid, enter_opt_page
auto_setup(__file__)
from poco.drivers.ios import iosPoco
poco = iosPoco()
ios_uninstall(ios_package_name)
ios_install(find_package('app_package','ipa'))
start_app(ios_package_name)
wait(Template(r"tpl1708924537998.png", record_pos=(-0.001, 0.001), resolution=(750, 1334)))
touch(Template(r"tpl1708924542876.png", record_pos=(0.183, 0.152), resolution=(750, 1334)))
wait(Template(r"tpl1709107932923.png", record_pos=(0.004, -0.001), resolution=(750, 1334)))
touch(Template(r"tpl1708924606474.png", record_pos=(-0.007, 0.147), resolution=(750, 1334)))
wait(Template(r"tpl1708924622398.png", record_pos=(0.376, -0.775), resolution=(750, 1334)))
touch(Template(r"tpl1708924631755.png", record_pos=(0.381, -0.779), resolution=(750, 1334)))
wait(Template(r"tpl1708924649542.png", record_pos=(-0.003, -0.513), resolution=(750, 1334)))
touch(Template(r"tpl1708924656255.png", record_pos=(0.003, 0.417), resolution=(750, 1334)))
wait(Template(r"tpl1708924679984.png", record_pos=(-0.228, -0.575), resolution=(750, 1334)))
touch(Template(r"tpl1708924671740.png", record_pos=(0.041, -0.24), resolution=(750, 1334)))
number, id = get_next_register_numberAndid()
text(number)
touch(Template(r"tpl1708925717602.png", record_pos=(-0.003, 0.147), resolution=(750, 1334)))
wait(Template(r"tpl1708925727656.png", record_pos=(-0.232, -0.581), resolution=(750, 1334)))
touch(Template(r"tpl1708925731870.png", record_pos=(-0.188, -0.293), resolution=(750, 1334)))
text(id)
touch(Template(r"tpl1708925772027.png", record_pos=(-0.003, 0.124), resolution=(750, 1334)))
wait(Template(r"tpl1708925779444.png", record_pos=(-0.252, -0.575), resolution=(750, 1334)))
text("0000")
wait(Template(r"tpl1708926053215.png", record_pos=(-0.092, -0.587), resolution=(750, 1334)))
touch(Template(r"tpl1708926066547.png", record_pos=(0.0, 0.276), resolution=(750, 1334)))
sleep(9.5)
wait(Template(r"tpl1708926126066.png", record_pos=(-0.005, -0.137), resolution=(750, 1334)))
touch(Template(r"tpl1708926093004.png", record_pos=(-0.277, 0.164), resolution=(750, 1334)))
touch(Template(r"tpl1708926095296.png", record_pos=(-0.277, 0.368), resolution=(750, 1334)))
touch(Template(r"tpl1708926097012.png", record_pos=(-0.273, 0.555), resolution=(750, 1334)))
touch(Template(r"tpl1708926100705.png", record_pos=(-0.005, 0.176), resolution=(750, 1334)))
touch(Template(r"tpl1708926101710.png", record_pos=(-0.007, 0.359), resolution=(750, 1334)))
touch(Template(r"tpl1708926102728.png", record_pos=(0.004, 0.555), resolution=(750, 1334)))
wait(Template(r"tpl1708926148471.png", record_pos=(-0.003, -0.136), resolution=(750, 1334)))
touch(Template(r"tpl1708926093004.png", record_pos=(-0.277, 0.164), resolution=(750, 1334)))
touch(Template(r"tpl1708926095296.png", record_pos=(-0.277, 0.368), resolution=(750, 1334)))
touch(Template(r"tpl1708926097012.png", record_pos=(-0.273, 0.555), resolution=(750, 1334)))
touch(Template(r"tpl1708926100705.png", record_pos=(-0.005, 0.176), resolution=(750, 1334)))
touch(Template(r"tpl1708926101710.png", record_pos=(-0.007, 0.359), resolution=(750, 1334)))
touch(Template(r"tpl1708926102728.png", record_pos=(0.004, 0.555), resolution=(750, 1334)))
wait(Template(r"tpl1708926510717.png", record_pos=(-0.007, 0.461), resolution=(750, 1334)))
update_next_register_numberAndid(number,id)
touch(Template(r"tpl1708926492707.png", record_pos=(-0.001, 0.741), resolution=(750, 1334)))
assert_exists(Template(r"tpl1708926624518.png", record_pos=(0.003, -0.603), resolution=(750, 1334)), "首次注册成功")
touch(Template(r"tpl1708926647129.png", record_pos=(-0.404, -0.764), resolution=(750, 1334)))
wait(Template(r"tpl1708926669547.png", record_pos=(-0.007, 0.069), resolution=(750, 1334)))
touch(Template(r"tpl1708926675163.png", record_pos=(0.0, 0.072), resolution=(750, 1334)))

assert_equal(poco("+966{}" .format(number)).get_name(),"+966{}" .format(number) , "number断言.")
update_registered_numberAndid(number,id)

