input_num = input("请输入一个5位数字:")
if len(input_num) != 5 or not input_num.isdecimal():
    print("错误提示：请输入一个5位纯数字")
else:
    reversed_num = input_num[::-1]
    if num == reversed_num:
        print("是回文数")
    else:
        print("不是回文数")
