num = input("숫자를 입력해 해주세요 : ") # 값 입력
nums = num.split() # 공백으로 나눠줌
num_list = [] # 배열생성
num_list = [int(i) for i in nums] # 배열에 정수형으로 nums 입력
it = len(num_list) # num_list의 전체 요소의 개수를 리턴

for i in range(0, it, 1): # i를 0 부터 it 까지 1 step
    for j in range(0, it-i-1, 1): # 배열 오른쪽부터 채워줌
        if num_list[j]>num_list[j+1]: # 왼쪽값이 더 큰경우
            tro = num_list[j] # 임시 함수에 num_list[j] 저장
            num_list[j] = num_list[j+1] # 값 변경
            num_list[j+1] = tro # 함수값으로 j+1 번지 변경


print(num_list) # 출력
            

    