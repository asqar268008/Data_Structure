import heapq
class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    
    def edge(self, vertex1, vertex2, weight, isDirected = False):
        self.vertex(vertex1)
        self.vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not isDirected:
            self.graph[vertex2][vertex1] = weight
    
    def removeVertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for node in self.graph:
            if vertex in self.graph[node]:
                del self.graph[node][vertex]
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            del self.graph[vertex1][vertex2]
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]

    def display(self):
        for key, value in self.graph.items():
            print(f"{key} => {value}")
        print()
    
    def shortestPath(self, startNode, endNode):
        distances = {v: float('inf') for v in self.graph}
        distances[startNode] = 0
        previous = {v: None for v in self.graph}

        pq = [(0, startNode)]

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_vertex == endNode:
                break

            for neighbour, weight in self.graph[current_vertex].items():
                new_dist = current_dist + weight

                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist
                    previous[neighbour] = current_vertex
                    heapq.heappush(pq, (new_dist, neighbour))
        path = []
        node = endNode
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        print("Shortest Path",path)
        print("Distance",distances[endNode])
        print()

weightedgraph = WeightedGraph()
weightedgraph.edge("Chennai", "Bangalore", 347)
weightedgraph.edge("Chennai", "Hyderabad", 627)
weightedgraph.edge("Chennai", "Coimbatore", 510)
weightedgraph.edge("Chennai", "Mumbai", 1330)
weightedgraph.edge("Chennai", "Kolkata", 1660)
weightedgraph.edge("Chennai", "Delhi", 2200)
weightedgraph.edge("Bangalore", "Hyderabad", 570)
weightedgraph.edge("Bangalore", "Mumbai", 985)
weightedgraph.edge("Bangalore", "Pune", 840)
weightedgraph.edge("Bangalore", "Mysore", 145)
weightedgraph.edge("Hyderabad", "Mumbai", 710)
weightedgraph.edge("Hyderabad", "Delhi", 1550)
weightedgraph.edge("Hyderabad", "Nagpur", 500)
weightedgraph.edge("Mumbai", "Pune", 150)
weightedgraph.edge("Mumbai", "Surat", 280)
weightedgraph.edge("Mumbai", "Ahmedabad", 525)
weightedgraph.edge("Mumbai", "Indore", 585)
weightedgraph.edge("Delhi", "Agra", 233)
weightedgraph.edge("Delhi", "Jaipur", 280)
weightedgraph.edge("Delhi", "Lucknow", 555)
weightedgraph.edge("Delhi", "Chandigarh", 250)
weightedgraph.edge("Kolkata", "Bhubaneswar", 440)
weightedgraph.edge("Kolkata", "Patna", 580)
weightedgraph.edge("Kolkata", "Ranchi", 400)
weightedgraph.edge("Pune", "Nagpur", 700)
weightedgraph.edge("Pune", "Ahmedabad", 660)
weightedgraph.edge("Pune", "Surat", 420)
weightedgraph.edge("Ahmedabad", "Jaipur", 675)
weightedgraph.edge("Ahmedabad", "Indore", 400)
print("Weighted Greaph")
weightedgraph.display()
weightedgraph.shortestPath("Chennai", "Ahmedabad")
weightedgraph.removeEdge("Chennai","Mumbai")
print("After Remove Edges")
weightedgraph.display()
weightedgraph.removeVertex("Mumbai")
print("After Remove Vertex")
weightedgraph.display()