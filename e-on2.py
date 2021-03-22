ang = 0
gimojji = int(input("값을 입력하세요 : ")) # gimojji 에 입력값 저장

while gimojji != 0: # gimojji가 0이 아닐때 반복
    ang += gimojji # ang + gimojji 를 ang에 저장
    gimojji = int(input("값을 입력하세요 : ")) # 입력값 입력

print("입력한 값의 합은", ang , "입니다.")