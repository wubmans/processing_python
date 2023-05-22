class Dijkstra:

    graph = None

    source = None
    target = None

    closedNodes = []
    openNodes = []

    currentNode = None
    

    def __init__(self, graph):
        self.graph = graph

        for node in self.graph.nodes:
            node.distance = -1


    def findPath(self, source, target):
        self.source = source
        self.source.isStart = True
        
        self.target = target
        self.target.isFinish = True

        self.source.distance = 0
        self.openNodes.append(self.source)

    def step(self):

        distance = -1

        for node in self.graph.nodes:
            node.shorterRoute = False

        if self.currentNode is not None:
            self.currentNode.isCurrentNode = False

        for node in self.openNodes:
            if distance == -1 or node.distance < distance:
                distance = node.distance
                self.currentNode = node

        self.currentNode.status = "closed"
        self.currentNode.isCurrentNode = True
        self.openNodes.remove(self.currentNode)

        neighbors = self.graph.getNeighbors(self.currentNode)

        for node in neighbors:
            edge = self.graph.getEdge(self.currentNode, node)
            distance = self.currentNode.distance + edge.weight
            if node.distance == -1 or node.distance > distance:
                node.shorterRoute = True
                node.distance = distance

            if node.status == "closed":
                continue

            # if node.status == "start":
            #     continue

            node.status = "open"
            
            self.openNodes.append(node)

        # neighbors = []

        # if self.currentNode == None:
        #     self.currentNode = self.source
        #     self.openNodes.append(self.currentNode)

        # if self.currentNode != None:
        #     self.currentNode.isCurrentNode = False

        
        
        
        # else:

        #     distance = -1
        #     bestNode = None

        #     for node in self.openNodes:
                
        #         if distance == -1 or node.distance < distance:
        #             distance = node.distance
        #             bestNode = node

        #     print(distance)
        #     self.currentNode = bestNode

        # self.currentNode.isCurrentNode = True

        # self.currentNode.status = "closed"
        # 
        # self.openNodes.remove(self.currentNode)

        # for node in neighbors:

        #     edge = self.graph.getEdge(self.currentNode, node)
        #     distance = self.currentNode.distance + edge.weight
        #     if node.distance == -1 or node.distance > distance:
        #         node.distance = distance

        #     if node.status == "closed":
        #         continue

        #     if node.status == "start":
        #         continue

        #     node.status = "open"
            
        #     self.openNodes.append(node)

        


        

