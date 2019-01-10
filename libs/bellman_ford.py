N,M = map(int,input().split()) #Nは頂点の数、Mは辺の数
E = [[int(_) for _ in input().split()] for i in range(M)]　# [[a1,b1,c1],[a2,b2,c3]]みたいな感じ,頂点a1から頂点b1までを重さc1で結ぶ


max_value = 99999*99999
scores = [max_value for i in range(N)]
scores[0] = 0

for a,b,c in E:
    #頂点の添え字を配列の添え字に合わせるために1を引く
    a -= 1 
    b -= 1
    if scores[b] >= scores[a] + c:#E[0]が頂点
        scores[b] = scores[a] + c

print(scores)


    

    