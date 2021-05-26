from bookmain import *
def menu():
    print("1 : 도서추가하겠는가?")
    print("2 : 검색해보겠는가?")
    print("3 : 개별적으로 검색하겠는가?")
    print("4 : 도서 정보 수정해볼래?")
    print("5 : 도서 삭제 해볼래?")
    print("6 : 현재 도서 목록을 보자")

    print("-----------------------------------------------------------")

menu()

def result():
    a = int(input("자 어떤걸 할까? : "))
    if a == 1:
        add()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    elif a == 2:
        search()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    elif a == 3:
        prisearch()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    elif a == 4:
        change()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    elif a == 5:
        delete()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    elif a == 6:
        hell_yeah()
        b = int(input("다시 실행하려면 1 아니면 2를 입력하세요."))
        if b == 1:
            menu()
            result()
        elif b == 2:
            print("프로그램이 종료되었습니다.")
            quit()
    else:
        print("멈춰 !!!!!!!!!!!!!!!!!!!!!!!!!")
    




result()
        

