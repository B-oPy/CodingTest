from string import ascii_uppercase

def solution(name) :
    letter = [x for x in name]
    alphabet = list(ascii_uppercase)
    front = list(alphabet[:12])
    back = list(reversed(alphabet[13:]))
    answer = 0
    alist = []

    for i in letter :
        if i == 'A' :
            alist.append(i)
    if len(alist) == len(letter) :
        return print(answer)

    if letter[1:-1] ==['A']*(len(letter)-2) :
        for k in [letter[0],letter[-1]] :
            if k in front :
                for l in front:
                    if k != l :
                        answer += 1
                        # print(l)
                    elif k == l :
                        break 
            else: 
                answer += 1
                for l in back:
                    if k != l :
                        answer += 1
                        # print(l)
                    elif k == l :
                        break
            answer += 1
            # print(answer)
        return print(answer -1)

    else : 
        for i in letter :
            if i in front :
                for j in front:
                    if i != j :
                        answer += 1
                        # print(j)
                    elif i == j :
                        break 
            else: 
                answer += 1
                for j in back:
                    if i != j :
                        answer += 1
                        # print(j)
                    elif i == j :
                        break
            answer += 1
            # print(answer)
        return print(answer-1)
        # answer = 0

solution('JEROEN')
# solution('JAN')
# solution("AAAAABBAAAAAAABAAA")