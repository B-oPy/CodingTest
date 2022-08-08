## 1번 풀이
# 1. set 자료형 사용(중복허용 x, 순서 x)
natural_num = set(range(1,10001)) # 1~10000까지 정수
generated_num = set() # 생성자 담을 set

for i in range(1,10001) :
    for j in str(i) :
        i += int(j)
        # 수를 받아서 각 자리수를 쪼갠 뒤 그 수에 더해줘서 생성자 생성
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num :
    print(i)
# 정수에서 생성자 뺴서 self number 구하고 오름차순 정렬, 줄 바꿔서 출력