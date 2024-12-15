import re

def count_alphabets(filename):
    with open(filename, 'r') as file:
        text = file.read()

    # 알파벳 문자만 추출하고 대소문자 구분 없이 처리
    text = re.sub(r'[^a-zA-Z]', '', text).upper()

    # 알파벳 빈도수 계산
    alphabet_count = {}
    for char in text:
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

    # 빈도수에 따라 내림차순 정렬
    sorted_alphabets = sorted(alphabet_count.items(), key=lambda item: item[1], reverse=True)

    # 결과 출력
    result = [item[0] for item in sorted_alphabets]
    print(result)

# 예시 사용법
count_alphabets('input_7_2.txt')
