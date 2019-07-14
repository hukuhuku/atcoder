N,A,B = map(int,input().split())

train = A*N
taxi  = B/N;

if taxi < train:
    print(taxi)
else:
    print(train)

