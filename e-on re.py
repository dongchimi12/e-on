on = int(input("수를 입력하세요 : "))
b = []
c = 0

while on != 0:
    b.append(on)
    on = int(input("수를 입력하세요 : "))
    c += 1


def angry(a):
    d = 0
    t = 0
    if on == 0 :
        while d != c :
          t += a[d]
          d += 1
    return t

print(b)
print("위의 수의 합은", angry(b),"입니다")


    