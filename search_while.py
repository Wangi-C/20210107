from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int:
    """시퀀스 a에서 key와 갑이 같은 원소를 선형 검색"""
    i = 0

    while True:
        if i == len(a):
            return -1 #검색 실패
        if a[i] == key:
            return i #검색 성공시 검사한 배열의 인덱스 반환
        i += 1

if __name__ == '__main__': #main함수 시작
    num = int(input('원소 수를 입력하세요 : '))
    x = [None]*num #원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))

    ky = int(input("검색할 값을 입력 : "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값이 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")