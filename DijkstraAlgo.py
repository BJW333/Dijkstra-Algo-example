import heapq

def dijkstra(graph, start):
    #initialize distances with infinity 
    #set the start node distance to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    #queue to hold the nodes to explore
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        #skip nodes that have already been visited with a shorter distance
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            #if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

#examples and usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)
