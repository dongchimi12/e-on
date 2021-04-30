on = int(input("수를 입력하세요 : "))
b = []
b.append(on)
count = 1
i = 1
count2 = 0
j = 0
if on > 1000 or on < 0:
    print("잘못된 수 입니다.")
else:
    while count != 10:
        on = int(input("수를 입력하세요 : "))
        b.append(on)
        if on <= 1000 and on >= 0:
            count += 1
            continue
        else:
            print("잘못된 값입니다.")    
            break
print(b)

def result():
    for i in range(0,len(b)):
         c = b[i] % 42
         b[i] = c
    return b
print("42로 나눈 값의 나머지 : ",result())

bb = sorted(result())

while i != 10:
    if bb[j] != bb[i]:
        count2 += 1
    i += 1
    j += 1

count2 += 1

print("다른 나머지의 총 개수 : " , count2)
        



    








    



