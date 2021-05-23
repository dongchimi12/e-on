def add():
    on = input("도서 추가(도서명, 저자, 출판연도, 출판사명, 장르 입력) : ")
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", "a") as f:
        f.write('\n' + on)
    print("추가완료")

def search():
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt","r") as inputDB:
         line = inputDB.readlines()

    string = input("검색할 도서를 입력하세요 : ")

    for l in line:
        if string in l:
            print(l, end = "")

def change():
    loca = "C:/Users/2020917/Desktop/개발/e-on/input.txt"
    new_text = ""
    t_word = input("바꿀 단어를 입력하세요 : ")
    c_word = input("뭐로 바꾸시겠습니까?")
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", "r") as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            new_string = l.strip().replace(t_word,c_word)
            if c_word:
                new_text += new_string + '\n'
            else:
                new_text += '\n'
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", "w") as f:
        f.write(new_text)
    print("단어가 변경되었습니다.")

def delete():
    a = input("삭제할 도서명을 입력하세요.")
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", 'r') as f:
        data = f.readlines()
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", 'w') as of:
        for i in data:
            if not i.startswith(a):
                of.write(i)
    print("삭제했습니다.")

def hell_yeah():
    with open("C:\\Users\\2020917\\Desktop\\개발\\e-on\\input.txt", 'r') as f:
        on = f.read()
        print(on)






    

    

    


