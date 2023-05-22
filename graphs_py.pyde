from graph import *
from dijkstra import *

graph = Graph()
dijkstra = None
stepCount = 1

def setup():
    global dijkstra
    global graph

    size(1000, 1000)

    points = 0

    while points < 20:
        x = random(800) + 100
        y = random(800) + 100

        minDistance = -1

        for node in graph.nodes:
            distance = (node.x - x) ** 2 + (node.y - y) ** 2
            if minDistance == -1 or distance < minDistance:
                minDistance = distance

        if (minDistance == -1 or minDistance > 8000):
            graph.addNode(x, y)
            points += 1
   
    for source in graph.nodes:

        connections = 0

        while connections < 2:

            connected = False
            attemptedDestinations = []

            while connected == False:

                minDistance = -1
                closestNode = None
                
                for destination in graph.nodes:

                    if destination == source:
                        continue

                    if destination in graph.getNeighbors(source):
                        continue

                    if destination in attemptedDestinations:
                        continue

                    distance = (source.x - destination.x) ** 2 + (source.y - destination.y) ** 2

                    if minDistance == -1 or distance <= minDistance:
                        closestNode = destination
                        minDistance = distance
                
                connected = graph.connect(source, closestNode, floor(random(10)))

                if connected == False:
                    attemptedDestinations.append(closestNode)

                if len(attemptedDestinations) > 7:
                    connected = True

            connections += 1

    dijkstra = Dijkstra(graph)
    dijkstra.findPath(graph.nodes[0], graph.nodes[9])

def mousePressed():
    global dijkstra
    global stepCount
    print("Step: " + str(stepCount))
    dijkstra.step()
    stepCount += 1
    
    
def draw():
    background(100)
    graph.draw()