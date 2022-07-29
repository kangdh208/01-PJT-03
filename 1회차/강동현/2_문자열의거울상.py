import sys

sys.stdin = open("_문자열의거울상.txt")

def mirror(letter): # 바꾸는 함수
    if letter == 'b':
        return 'd'
    elif letter == 'd':
        return 'b'
    elif letter == 'p':
        return 'q'
    else:
        return 'p'

T = int(input())
for z in range(T):
    string = input()
    gnirts = string[::-1] #뒤집고
    newstr =''
    for i in range(len(gnirts)):
        newstr += mirror(gnirts[i]) #뒤집어 더하기
    print(f'#{z+1} {newstr}')