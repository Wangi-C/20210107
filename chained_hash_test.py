from enum import Enum #Enum?
from chained_hash import chainedHash

Menu = Enum('menu',['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() ->Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep = '  ', end="") #??
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)