from itertools import combinations

def solution(number, k):
    num_list=[]
    num = list(combinations(number,len(number)-k))
    
    for i in num:
        num_list.append("".join(i))
        
    a = sorted(num_list)
    
    answer = a[-1]

    
    return answer

# 순열을 이용하여 조합한 뒤, 정렬하는 방법으로 접근
# 7.12 33%
