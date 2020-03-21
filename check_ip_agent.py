import telnetlib

ip_list = []
port_list = []

# 验证代理ip是否可用
def check_ip_agent(ip_check,port_check):
    try:
        telnetlib.Telnet(ip_check, port=port_check, timeout=20)
    except:
        print('无效')
        return False,False
    else:
        print('有效')
        return ip_check,port_check

# 选择代理ip
def choice_ip_agent():
    # 读取txt文件
    with open("ip_agent.txt","r") as f:
        for line in f:
            # 消除多余的换行符
            ip_agent = line.rstrip()
            # 将代理ip以":"分割成ip_0和port_0
            ip_0,port_0 = ip_agent.split(':', 1)
            # 将ip_0和port_0分别存入ip_list和port_list列表中
            ip_list.append(ip_0)
            port_list.append(port_0)

    # 选择代理ip
    index = int(input("请选择第几个代理ip："))
    ip_choice,port_choice = check_ip_agent(ip_list[index],port_list[index])
    return ip_choice,port_choice

# main()
ip,port = choice_ip_agent()
print("ip: %s" % ip)
print("port: %s" % port)