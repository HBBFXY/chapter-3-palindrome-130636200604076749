num = input("请输入一个5位数字:")
if len(num) != 5 or not num.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
