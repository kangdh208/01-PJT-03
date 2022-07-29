import sys

sys.stdin = open("_신용카드만들기2.txt")

def dashchk(oldcard): #-없애기
    card = ''
    for i in range(len(oldcard)):
        if oldcard[i] != '-':
            card += oldcard[i]
    return card

def numchk(cardnum): #첫숫자가 3569니?
    if len(cardnum) == 16: #길이는?16이야?
        if cardnum[0] in '34569':
            return 1 #어, 둘다맞아
        else:
            return 0 #아니
    else:
        return 0 #아뉜데

T = int(input())
for z in range(T):
    number = input()
    cardnumber = dashchk(number) # dash없애고
    print(f'#{z+1} {numchk(cardnumber)}') #확인하기