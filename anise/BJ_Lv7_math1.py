#1712 손익분기점
A, B, C = map(int, input().split())

if B>=C :
    print(-1)
else :
    print(A//(C-B) +1)

# 2292 벌집
n = int(input())
layer = 1
rooms = 1
while n > rooms :
    rooms += 6*layer
    layer += 1
print(layer)    

# 1193 분수찾기
n = int(input())
layer = 1
fracs = 1
while n > fracs :
    layer += 1
    fracs += layer

if layer % 2 == 0 :
    up = layer - (fracs - n)
    down = (layer + 1) - up
else :
    down = layer - (fracs - n)
    up = (layer + 1) - down
print(str(up) + "/" + str(down))    


