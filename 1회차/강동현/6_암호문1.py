import sys

sys.stdin = open("_암호문1.txt")

for z in range(10):
    A = int(input())
    B = list(map(int,input().split()))
    C = int(input())
    D = list(input().split('I ')) #I로 쪼개자
    D = D[1:] # 맨앞 잔챙이 치우기
    for i in range(len(D)): # 명령어 쪼개서 리스트화
        element = list(map(int, D[i].split()))
        NewD = []
        NewD.append(element)
        idx = NewD[0][0] # 언제부터 바꿀꺼야
        if NewD[0][0]: #중간이면 B를 자르고
            B = B[:idx] + NewD[0][2 : 3+C] + B[idx:]
        else: # 처음부터?? 그럼 B를 뒤로
            B = NewD[0][2 : 3+C] + B
    password = []
    for i in range(10): #리스트를 문자열로
        password.append(str(B[i]))
    answer = ' '.join(password)
    print(f'#{z+1} {answer}')