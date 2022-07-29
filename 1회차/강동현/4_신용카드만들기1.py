import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for z in range(T):
    lst = list(map(int,input().split()))
    oddsum = 0
    evensum = 0
    n=0
    for i in range(0, 15, 2): #홀수합
        oddsum += 2*lst[i]
    for i in range(1,14,2): #짝수합
        evensum += lst[i]
    numsum = (oddsum + evensum)%10 #뒷자리가 몇이야
    n = (10-numsum)%10 #10의 보수 사용
    print(f'#{z+1} {n}')