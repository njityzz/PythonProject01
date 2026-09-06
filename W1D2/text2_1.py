# 简单用户登录系统

# 预设的正确用户名和密码（可以按需修改）
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "123456"

# 最大尝试次数
MAX_ATTEMPTS = 3

# 记录当前尝试次数
attempts = 0

print(f"欢迎登录！您有 {MAX_ATTEMPTS} 次尝试机会。")

while attempts < MAX_ATTEMPTS:
    # 输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 验证
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("登录成功！欢迎回来。")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"用户名或密码错误，您还有 {remaining} 次机会。")
        else:
            print("错误次数已达上限，登录失败。")