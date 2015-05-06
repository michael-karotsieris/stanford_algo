

def bfs(G , S):# graph = G , start_vertex = s , supose G is a dictionary
	graph_queue = [S]
	visited = []
	print "Graph Queue initial"
	print graph_queue
	while graph_queue:
		next_node = G[graph_queue.pop(0)]
		for edge in next_node :
			if edge not in visited:
				visited.append(edge)
				print "Visited Node: " + str(edge)
				graph_queue.append(edge)
					
					
					
