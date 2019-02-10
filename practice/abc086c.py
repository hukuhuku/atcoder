N = int(input())

prev_t = 0
prev_x = 0
prev_y = 0

res = "Yes"
for i in range(N):
    t,x,y = map(int,input().split()
    
    distance = abs(x-prev_x) + abs(y-prev_y)

    if t - prev_t < distance:
        res = "No"
    

print(res)



