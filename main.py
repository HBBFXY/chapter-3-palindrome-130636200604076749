s = input("请输入一个5位数字：")
if len(s) != 5 or not s.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    is_palindrome = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1 - i]:
            is_palindrome = False
            break
    print("是回文数" if is_palindrome else "不是回文数")
