#TODO:Copy.
"""版权声明：

   本开源项目由Rain编写，版权均属Rain所有，请勿将此项目用于赚钱。

    Copy。2022-2023 Rain
"""

#TODO:正片
import pymysql
user=["admin","user1"]
user_id={"admin":114514919810,"user1":111111111111}
id_user={114514919810:"admin",111111111111:"user1"}
user_p={"admin":"114514","user1":"1"}
user_jihuo={"admin":True,"user1":False}
money={"admin":114514,"user1":0}
id_jihuo={114514919810:True,1111111111111:False}
a=0
class sys_cz:
    def system(self,user_name,password):
        if user_name in user:
            if password == user_p[user_name]:
                print("欢迎回来，尊敬的",user_name,"。")
                while True:
                    print("1.存钱 2.取钱 3.转账 4.查看余额 5.退出 6.切换账号")
                    a=int(input("请输入："))
                    if a==1:
                        m=int(input("请输入要存的金额："))
                        money[user_name]= money[user_name] + m
                        print("成功")
                    elif a==2:
                        m = int(input("请输入要取的金额："))
                        if m<=money[user_name]:
                            money[user_name] = money[user_name] - m
                            print("成功")
                    elif a==3:
                        id=int(input("请输入对方id："))
                        if id in id_user:
                            if id_jihuo[id]==True:
                                m=int(input("请输入金额："))
                                if m<money[user_name]:
                                    money[user_name]= money[user_name] - m
                                    print("成功")
                                else:
                                    print("失败")
                            else:
                                print("账号被封")
                        else:
                            print('没有此id')
                    elif a==4:
                        print(money[user_name])
                    elif a==5:
                        exit()
                    elif a==6:
                        b=sys_cz.login(1)

            else:
                print("错误，请登录")
                return
        else:
            print("错误，请登录。")
            return
    def login(self):
        over = 4
        while True:
            u = input("请输入你的名字:")
            id = int(input("请输入你的卡号："))
            if u in user:
                if id == user_id[u]:
                    while True:
                        p = input("请输入你的密码：")
                        if p == user_p[u] and over > 0:
                            if user_jihuo[u] == True:
                                print("登陆成功")
                                sys_cz.system(self=1, user_name=u, password=p)
                            else:
                                print("哥们，你这账号有问题啊。")
                                sys_cz.welcom(1)
                        else:
                            if over > 0:
                                print("密码有问题。还可以验证", over, "次")
                                over = over - 1
                            else:
                                print("由于多次输入账号密码未成功，请明天再操作。")
                                user_jihuo[u] = False
                                id_jihuo[id] = False
                                sys_cz.welcom(1)
                else:
                    print('没有此账号')
            else:
                print('没有此账号。')
    def reg(self):
        while True:
            u=input("请输入你想要的账号名：")
            id=int(input("请输入你想要的银行卡号："))
            p=input("请输入你想设置的密码：")
            if u not in user:
                id_nub=0
                for i in str(id):
                    id_nub+=1
                if id_nub==12:
                    user.append(u)
                    user_id[u]=id
                    user_p[u]=p
                    money[u]=0
                    id_user[id]=u
                    id_jihuo[id]=True
                    user_jihuo[u]=True
                    print("注册成功")
                    sys_cz.system(self=1,user_name=u,password=p)
                else:
                    print("卡号不够12位")
            else:
                print("用户名已存在")
    def welcom(self=1):
        print("""        ______________________________________________________________________
        |                                                                    |
        |                     欢迎来到python银行                               |
        |                                                                    |
        |                                                                    |
        |                                                                    |
        |                        1.登录                                       |
        |                                                                    |
        |                                                                    |
        |                        2.注册                                       |
        |                                                                    |
        |                                                                    |
        |                        3.退出                                       |
        |                                                                    |
        |                                                                    |
        |                                                                    |
        ______________________________________________________________________""")
        while True:
            a=int(input("请输入序号："))
            if a==1:
                sys_cz.login(1)
            elif a==2:
                sys_cz.reg(1)
            elif a==3:
                exit()
sys_cz.welcom(1)