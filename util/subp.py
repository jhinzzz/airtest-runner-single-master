import re
import subprocess
import time


def command(cmd):
    # 定义要执行的 tidevice 命令
    tidevice_command = cmd

    # 使用 subprocess 模块执行命令
    process = subprocess.Popen(tidevice_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取命令执行结果
    output, error = process.communicate()

    if error:
        print("Error executing command:", error.decode())
        raise SystemExit()
    else:
        return output.decode('latin1')

def connect_wda():
    device_uid = command('tidevice list')
    # 去掉转义字符和空格换行符
    cleaned_str = device_uid.replace("\n", "").replace("\r", "")

    # 使用空格分割字符串
    split_data = cleaned_str.split()

    # 将分割后的单词用逗号连接起来
    result_str = ",".join(split_data)
    # 定义正则表达式模式
    pattern = r'ConnType(.*?)(?=,)'

    # 使用正则表达式进行匹配
    result = re.search(pattern, result_str).group(1)
    # 定义要写入到 bat 文件中的内容
    bat_content = """
    @echo off
    tidevice -u {device_id} wdaproxy -B com.facebook.WebDriverAgentRunner.xctrunner --port 8100
    """

    # 使用字符串格式化替换设备号
    formatted_bat_content = bat_content.format(device_id=result)

    # 指定 bat 文件路径
    bat_file_path = "start_wda.bat"

    # 将内容写入到 bat 文件中
    with open(bat_file_path, "w") as file:
        file.write(formatted_bat_content)

    print(f"已成功创建 {bat_file_path} 文件")

    # 调用批处理文件
    subprocess.Popen("start_wda.bat", shell=True,
                     creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
    time.sleep(5)

def output_app_version():
    app_list = command('tidevice applist')
    applist = app_list.split('\r\n')
    filtered_data = list(filter(lambda x: "com.tiqmo.wallet.ksa.uat" in x, applist))
    if filtered_data:
        last_space_index = filtered_data[0].rfind(' ')
        if last_space_index != -1:
            result = str(filtered_data[0][last_space_index + 1:])
            return result
        else:
            raise SystemExit()
    else:
        pass

def ios_uninstall(ios_package_name):
    command('tidevice uninstall {}' .format(ios_package_name))

def ios_install(ios_package_loc):
    command('tidevice install {}' .format(ios_package_loc))

def ios_launch(ios_package_name):
    command('tidevice launch {}' .format(ios_package_name))

if __name__ == '__main__':
    connect_wda()