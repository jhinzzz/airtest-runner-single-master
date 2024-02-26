import subprocess

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
    print(output_app_version())