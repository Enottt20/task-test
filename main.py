import itertools


def get_expressions(expected_result: int, is_single_result: bool = False):
    number_range = range(0, 10)
    initial_string = ''.join(str(x) for x in number_range)
    initial_string_length = len(initial_string)
    options = list(itertools.product(['+', '-', ''], repeat=initial_string_length - 1))
    success_result_list = []
    for option in options:
        expression = ''.join(
            [digit + option[i] if i < len(initial_string) - 1 else digit for i, digit in enumerate(initial_string)])
        if not expression.startswith('01'):
            result = eval(expression)
            if result == expected_result:
                success_result_list.append(expression)
            if is_single_result:
                return success_result_list
    return success_result_list




if __name__ == '__main__':
    result_list = get_expressions(expected_result=200)
    for result_expression in result_list:
        calculated_result = eval(result_expression)
        print(f"{result_expression} = {calculated_result}")