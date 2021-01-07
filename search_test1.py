from search_while import seq_search

print("실수를 검색한다")
print("end를 입력하면 종료합니다.")

number = 0
x = []

while True:
    s = input(f"x[{number}]")
    if s == "end":
        break
    x.append(float(s))
    number += 1

ky = float(input("검색할 값을 입력 : "))

idx = seq_search(x, ky)
if idx == -1:
    print("검색값이 존재하지 않는다")
else:
    print(f"검색한 값은 x[{idx}]에 있습니다.")

