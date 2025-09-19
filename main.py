num_str = input("请输入一个5位数字:")
if len(num_str) != 5 or not num_str.isdigit():
    print("错误提示：请输入一个5位纯数字")
else:
    is_palindrome = True
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[len(num_str) - 1 - i]:
            is_palindrome = False
            break
    print("是回文数" if is_palindrome else "不是回文数")
