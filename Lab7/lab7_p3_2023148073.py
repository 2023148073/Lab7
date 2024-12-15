class list_D2(list):
    def __init__(self, input_list):
        # 입력 리스트의 차원이 2차원이 아닌 경우 에러 발생
        if not all(isinstance(i, list) for i in input_list):
            raise ValueError("[ERROR]: list is not 2D.")

        # 내부 리스트들의 길이가 동일하지 않은 경우 에러 발생
        if len(set(len(i) for i in input_list)) > 1:
            raise ValueError("[ERROR]: inner lists are not same in length.")

        super().__init__(input_list)

    def __str__(self):
        return f"list_2D: {len(self)}*{len(self[0])}"

    def transpose(self):
        return list_D2([list(row) for row in zip(*self)])

    def __matmul__(self, other):
        if len(self[0]) != len(other):
            raise ValueError("[ERROR]: [a][b]*[c][d] not b==c.")

        result = list_D2([[sum(a * b for a, b in zip(row, col)) for col in zip(*other)] for row in self])
        return result

    def avg(self):
        total = sum(sum(row) for row in self)
        count = sum(len(row) for row in self)
        return total / count


# 테스트 코드
if __name__ == "__main__":
    try:
        list1 = list_D2([1, 2, 3])
    except Exception as e:
        print(e)

    try:
        list1 = list_D2([[1, 2], [2, 3], [1, 2, 3]])
    except Exception as e:
        print(e)

    list1 = list_D2([[1, 2], [2, 3], [1, 2]])
    print(list1)

    list1_ = list_D2([[1, 2], [2, 3], [1, 2]])
    list2 = list_D2([[1, 2, 3], [1, 2, 3]])
    print(list1.transpose())
    try:
        list3 = list1 @ list1_
    except Exception as e:
        print(e)
    list3 = list1 @ list2
    print(list3)
    print(list(list3))
    print(list1.avg())
