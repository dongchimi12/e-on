ang = [] # 빈 배열 값
a = int(input("숫자를 입력하세요 : ")) # 입력값을 a에 저장
b = 0 #초기값
result = 0 #초기값

while a != 0: # a가 0이 아니면 반복
    ang.append(a) # ang에 입력값 a를 0~1번지부터 저장
    result += ang[b] # result + ang[b]번지를 더한 값을 result에 저장
    b += 1 # b + 1 를 b에 저장
    a = int(input("숫자를 입력하세요 : ")) # 입력값을 다시 받음

print("입력값의 합은", result, "입니다") # 최종값 출력


    

    

