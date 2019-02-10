class BellmanFord:
    def __init__(self, graph, num_v, start_point):
        """
        graph : [[a1,b1,c1],[a2,b2,c2],‥]みたいな3次元配列のリスト,a1からb1までのコストはc1
        num_v :頂点の数
        start_point :スタート地点(a1)
        """
        self.num_v = num_v
        self.graph = graph
        self.start_point = start_point
 
 
    def execute(self):
        dist = [float("inf") for _ in range(self.num_v)]
        dist[self.start_point] = 0

        negative = [False for _ in range(self.num_v)]

        for i in range(self.num_v - 1):
            for start, end, cost in self.graph:
                if dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost

        #負の経路がないなら|V-1|以上の繰り返しで最短経路の更新は行われない、負の経路の検出
        for i in range(self.num_v):
            for start, end, cost in self.graph:
                if dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost
                    negative[end] = True
                if negative[start]:
                    negative[end] = True
        return dist, negative
 
 



    

    