class graph:
    def __init__(self):
        self.graph = {}
    
    def vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return
    
    def edge(self, vertex1, vertex2, isDirected = False):
        self.vertex(vertex1)
        self.vertex(vertex2)
        self.graph[vertex1].extend([vertex2])
        if not isDirected:
            self.graph[vertex2].extend([vertex1])
    
    def display(self):
        for key, value in self.graph.items():
            print(f"{key} => {value}")
    
    def getVertex(self):
        for i in self.graph:
            print(i)

    def getEdges(self):
        for key, value in self.graph.items():
            for vertex in value:
                print(f"({key},{vertex})") 
    
    def deleteVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key, value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
    
    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

graph1 = graph()
graph1.edge("A","B")
graph1.edge("B","C")
graph1.edge("B","D")
graph1.edge("C","D")
graph1.display()
graph1.getVertex()
graph1.getEdges()
graph1.deleteVertex("C")
print("After remove Vertex")
graph1.display()
graph1.deleteEdge("B","D")
print("After remove Edges")
graph1.display()