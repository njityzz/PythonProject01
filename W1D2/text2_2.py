# 进制转换（手动实现）

# ---------- 十进制转二进制 ----------
def dec_to_bin(n):
    """
    将十进制整数 n 转换为二进制字符串（手动实现）
    支持负数（输出带负号）
    """
    if n == 0:
        return "0"

    is_negative = False
    if n < 0:
        is_negative = True
        n = -n

    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n //= 2

    # 余数是从下往上读，所以反转
    binary_str = ''.join(reversed(binary_digits))
    return '-' + binary_str if is_negative else binary_str


# ---------- 十进制转十六进制 ----------
def dec_to_hex(n):
    """
    将十进制整数 n 转换为十六进制字符串（手动实现）
    支持负数（输出带负号）
    """
    if n == 0:
        return "0"

    is_negative = False
    if n < 0:
        is_negative = True
        n = -n

    hex_chars = "0123456789ABCDEF"
    hex_digits = []
    while n > 0:
        remainder = n % 16
        hex_digits.append(hex_chars[remainder])
        n //= 16

    hex_str = ''.join(reversed(hex_digits))
    return '-' + hex_str if is_negative else hex_str


# ---------- 用户交互 ----------
if __name__ == "__main__":
    try:
        num = int(input("请输入一个十进制整数："))
        print(f"二进制：{dec_to_bin(num)}")
        print(f"十六进制：{dec_to_hex(num)}")
    except ValueError:
        print("输入无效，请输入一个整数。")