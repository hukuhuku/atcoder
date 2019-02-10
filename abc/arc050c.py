def gcd(a, b):
    #最大公約数を求める、ユークリッドの互除法を使う
    while b:
        tmp = a%b
        a = b
        b = tmp
    return a

def lcm(a, b):
	return a * b // gcd (a, b)

A,B,M = map(int,input().split())

A = int(str(1)*A)
B = int(str(1)*B)

print(lcm(A,B)%M)

