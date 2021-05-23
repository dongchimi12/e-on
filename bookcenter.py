from bookmain import *

print("1 : 도서추가하겠는가?")
print("2 : 검색해보겠는가?")
print("3 : 도서 정보 수정해볼래?")
print("4 : 도서 삭제 해볼래?")
print("5 : 현재 도서 목록을 보자")

print("-----------------------------------------------------------")

def result():
    a = int(input("자 어떤걸 할까? : "))
    if a == 1:
        add()
    elif a == 2:
        search()
    elif a == 3:
        change()
    elif a == 4:
        delete()
    elif a ==5:
        hell_yeah()
    else:
        print("멈춰 !!!!!!!!!!!!!!!!!!!!!!!!!")

result()

        

