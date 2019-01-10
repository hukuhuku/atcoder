def gcd(a, b):
    #最大公約数を求める、ユークリッドの互除法を使う
    while b:
		a, b = b, a % b
	return a



def lcm(a, b):
	return a * b // gcd (a, b)
    