num = input("请输入一个5位数字：")
if len(num) != 5 or not num.isdigit():
    print("错误提示：请输入一个5为纯数字")
else:
    reversed_num = ""
    for char in num:
        reversed_num = char + reversed_num
    print("是回文数" if num == reversed_num else "不是回文数")
