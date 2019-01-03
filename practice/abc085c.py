#N,Y = map(int,input().split())
N,Y = 9,45000
#x+y+z = n
#10000x + 5000y + 1000z = Y

flag = True
for x in range(N+1):
    for y in range(N-x+1):
        z = (N-(x+y))
        print(x,y,z)
        if 10000*x + 5000*y + 1000*z == Y:
            a,b,c = x,y,z
            flag = False
            break
            
if flag:
  print(-1,-1,-1)
else:
  print(a,b,c)
  