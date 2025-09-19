def is_valid_input(input_str):
    """校验输入是否为5位纯数字"""
    return len(input_str) == 5 and input_str.isdigit()

def check_palindrome(number_str):
    """判断字符串是否为回文"""
    return number_str == number_str[::-1]

# 主程序逻辑
if __name__ == "__main__":
    # 更明确的输入提示
    user_input = input("请输入一个5位数字（例如：12321）：")
    
    # 先校验输入合法性
    if not is_valid_input(user_input):
        print("错误提示：请输入一个5位纯数字")
    else:
        # 执行回文判断并输出结果
        result = "是回文数" if check_palindrome(user_input) else "不是回文数"
        print(result)
