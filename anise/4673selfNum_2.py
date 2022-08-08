## 2번 풀이
# 생성자를 만드는 함수
def genNum(n) :
    for i in list(str(n)) :
        n += int(i)
    return n

generated_num = []

# 문제 조건 범위에서 생성자인 수 리스트에 넣어줌
for i in range(1,10001) :
    generated_num.append(genNum(i))

# 생성자를 제외한 수 = self number
for j in range(1,10001) :
    if j in generated_num :
        pass
    else :
        print(j)