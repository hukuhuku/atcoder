import numpy as np
N,K = map(int,input().split())

h = [int(input()) for i in range(N)]
h.sort()


res = min(list((np.array(h[K-1:]) - np.array(h[:-K+1]))))
print(res)
