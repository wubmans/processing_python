    
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

class Graph:
    

    nodes = []
    edges = []
    
    def __init__(self):
        pass
    
    def addNode(self, x, y):
        
        node = Node(x, y)
        self.nodes.append(node)
                
                
    def draw(self):
            
        for edge in self.edges:
            edge.draw()

        for node in self.nodes:
            node.draw()
            
    def connect(self, source, target, weight):
        for edge in self.edges:
            if edge.source == source and edge.target == target:
                continue
            if edge.target == source and edge.source == target:
                continue
            if intersect(edge.source, edge.target, source, target):
                return False

        self.edges.append(Edge(source, target, weight))
        return True

    def getNeighbors(self, node):
        neighbors = []

        for edge in self.edges:
            if edge.source == node:
                neighbors.append(edge.target)
            if edge.target == node:
                neighbors.append(edge.source)

        return neighbors

    def getEdge(self, source, target):

        for edge in self.edges:
            if edge.source == source and edge.target == target:
                return edge
            if edge.target == source and edge.source == target:
                return edge

class Node:

    status = "unvisited"
    isCurrentNode = False
    isStart = False
    isFinish = False
    shorterRoute = False
    distance = -1
    x = None
    y = None
    
    neighbors = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
  
    def draw(self):
        noStroke()

        if self.status == "target":            
            fill(209,17,65)
        elif self.status == "start":
            fill(0,177,89)
        elif self.status == "closed":
            fill(243,119,53)
        elif self.status == "open":
            fill(255,196,37)
        else:
            fill(200)
    	
            
        ellipse(self.x, self.y, 30, 30)
        textAlign(CENTER, CENTER)
        fill(20)
        text(self.distance, self.x, self.y); 
        
        if self.isCurrentNode == True:
             stroke(240)
             noFill()
             ellipse(self.x, self.y, 32, 32)

        if self.isStart == True:
             stroke(0,177,89)
             noFill()
             ellipse(self.x, self.y, 32, 32)

        if self.isFinish == True:
             stroke(209,17,65)
             noFill()
             ellipse(self.x, self.y, 32, 32)

        if self.status == "closed" and self.shorterRoute == True:
             stroke	(0,174,219)
             noFill()
             ellipse(self.x, self.y, 32, 32)

class Edge:
    
    source = None
    target = None
    weight = 0
    
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    
    def draw(self):
        stroke(150)
        strokeWeight(4)
        line(self.source.x, self.source.y, self.target.x, self.target.y)

        textSize(12)

        x =  abs(self.source.x - self.target.x) / 2 + min(self.source.x, self.target.x)
        y =  abs(self.source.y - self.target.y) / 2 + min(self.source.y, self.target.y)


        noStroke()
        fill(60)
        rect(x - 6, y - 6, 16, 16)

        textAlign(CENTER, CENTER)
        fill(150)
        text(self.weight, x, y); 




