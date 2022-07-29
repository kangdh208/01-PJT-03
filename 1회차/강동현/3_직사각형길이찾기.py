import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for z in range(T):
    a, b, c = map(int,input().split())
    if a == b and b == c and c == a: # 정사각형
        print(f'#{z+1} {a}') 
    elif a==b and a !=c: # 직사각형
        print(f'#{z+1} {c}')
    elif a==c and a != b:
        print(f'#{z+1} {b}')
    else:
        print(f'#{z+1} {a}')