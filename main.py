# 输入并校验
s = input("请输入一个5位数字：")
if len(s) != 5 or not s.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    # 切片反转判断
    print("是回文数" if s == s[::-1] else "不是回文数")
