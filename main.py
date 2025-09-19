def is_valid_input(input_str):
    return len(input_str) == 5 and input_str.isdigit()

def check_palindrome(number_str):
    return number_str == number_str[::-1]
if __name__ == "__main__":
    user_input = input("请输入一个5位数字（例如：12321）：")
    if not is_valid_input(user_input):
        print("错误提示：请输入一个5位纯数字")
    else:
        result = "是回文数" if check_palindrome(user_input) else "不是回文数"
        print(result)
