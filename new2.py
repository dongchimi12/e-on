a = list(map(int,input("배열 입력 : ").split(",")))


def cool(on):
     b = list(map(int,input("자를 시작, 끝, 자른 수의 번호 ").split(",")))
     on = on[b[0]-1 : b[1]-1]
     on.sort()
     c = on[b[2]-1]
     return c

print("자른 수 중에서 k번쨰 수는 ", cool(a) ,"입니다.") 
    