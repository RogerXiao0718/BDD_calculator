import re


def calculator(expression):
    mathematical_regex = r'[^a-zA-Z]*'
    # This RegExp match operation is for prevent user enter unsafe expression that could damage the system.
    # 此正規表達式的匹配運算是為了避免使用者輸入會危害系統的指令
    filtered_expression = re.match(mathematical_regex, expression).group(0)
    # use eval to do calculation using python
    try:
        return eval(filtered_expression)
    except Exception as e:
        return "Invalid Input"

def calculator_app():
    isAgreeToCalculate = False
    while not isAgreeToCalculate:
        expression = input("Please enter the expression you want to calculate: ")
        calculateDesireCheckInput = input("Please enter '=' to continue calculation: ")
        isAgreeToCalculate = True if calculateDesireCheckInput == '=' else False
    result = calculator(expression)
    print(result)


if __name__ == '__main__':
    calculator_app()