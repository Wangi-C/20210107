# 이진 검색 알고리즘

from typing import Any, Sequence #typing? Any, Sequence?

def bin_search(a : Sequence, key : Any) -> int:
    pl = 0 #검색범위 맨 앞 원소의 인덱스
    pr = len(a)-1 #맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc -1
        if pl > pr:
            break
    return -1

if __name__ == '__main__': #main함수 시작
    num = int(input('원소 수를 입력하세요 : '))
    x = [None]*num #원소 수가 num인 배열 생성

    print("배열 데이터를 오름차순으로 입력")

    x[0] = int(input("x[0] : "))

    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i - 1]:
                break

    ky = int(input("검색할 값을 입력 : "))

    idx = bin_search(x, ky)

    if idx == -1:
        print("검색값이 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")