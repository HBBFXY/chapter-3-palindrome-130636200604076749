# 从键盘获取输入
num_str = input("请输入一个5位数字：")

# 校验输入是否为5位且纯数字
if len(num_str) != 5 or not num_str.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    # 利用字符串切片反转并判断回文
    if num_str == num_str[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
