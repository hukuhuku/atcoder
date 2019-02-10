N = int(input())
L = list(map(int,input().split()))


a = max(L)
L.remove(a)

if a >= sum(L):
    print("No")
else:
    print("Yes")