import re

def find_functions_and_calls(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    function_pattern = re.compile(r'def (\w+)\(')
    call_pattern = re.compile(r'(\w+)\(')

    functions = {}
    for i, line in enumerate(lines):
        function_match = function_pattern.search(line)
        if function_match:
            function_name = function_match.group(1)
            functions[function_name] = {'def': i + 1, 'calls': []}

    for i, line in enumerate(lines):
        call_matches = call_pattern.findall(line)
        for call in call_matches:
            if call in functions:
                functions[call]['calls'].append(i + 1)

    for function, details in functions.items():
        print(f"{function}: def in {details['def']}, calls in {details['calls']}")

# 예시 사용법
find_functions_and_calls('input_7_1.txt')
