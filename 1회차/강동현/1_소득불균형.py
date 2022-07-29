import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for z in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    avg = sum(lst)/n #평균구하기
    cnt = 0 
    for i in range(len(lst)):
        if lst[i] <= avg: #작아?
            cnt +=1 #너 추가
    print(f'#{z+1} {cnt}')