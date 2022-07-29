import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for z in range(T):
    testinput = int(input())
    scoreinput = list(map(int, input().split())) 
    cnt = {} # 점수 개수 일일이 센다 >> 딕셔너리
    for i in scoreinput:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    maxkey = max(cnt, key = cnt.get) #최댓값 찾기
    maxlst = [k for k, v in cnt.items() if max(cnt.values())==v] # 여러개야?
    print(f'#{z+1} {max(maxlst)}') #그럼 제일 큰거