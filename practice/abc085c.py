N,Y = map(int,input().split())

is_combination = False

for x in range(N+1):
    for y in range(N-x+1):
        z = (N-(x+y))
        if 10000*x + 5000*y + 1000*z == Y:
            a,b,c = x,y,z
            is_combination = True
            break
            
if is_combination:
  print(a,b,c)
else:
  print(-1,-1,-1)
  