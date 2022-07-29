import sys

sys.stdin = open("_암호문1.txt")

for z in range(10):
    A = int(input())
    B = list(map(int,input().split()))
    C = int(input())
    D = list(input().split('I '))
    D = D[1:]
    for i in range(len(D)): # 명령어 쪼개서 리스트화
        element = list(map(int, D[i].split()))
        NewD = []
        NewD.append(element)

        for i in range(C):
            x = NewD[0][0]
            y = NewD[0][1]
            s = NewD[0][2:] # 이게 문제같은데
            for j in range(y):
                B.insert(x+j, s[j]) #insert 이렇게쓰면안되나?
    password = []
    for i in range(10):
        password.append(str(B[i]))
    password = ' '.join(password)
    print(f'#{z+1} {password}') # 