"""
출근 하시면!!!
아침업무로
배달 온 상자안에 물건을 전부 까서
사과는 냉장실에
아이스크림은 냉동실에 넣어 주시고,
나머지는 폐기처분 해주세요.
"""


def 아침업무(상자):
    for 물건 in 상자:
        if 물건 == "사과":
            print(f"'{물건}' 냉장실에 넣기")
        elif 물건 == "아이스크림":
            print(f"'{물건}' 냉동실에 넣기")
        else:
            print(f"'{물건}'은 폐기 처분")

출근 = True

if (출근):
    배달상자 = ["사과", "콩", "콩", "강낭콩", "사과"]
    아침업무(배달상자)
