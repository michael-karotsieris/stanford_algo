

def bfs(G , S):# graph = G , start_vertex = s , supose G is a dictionary
	graph_queue = [S]
	visited = []
	print "Graph Queue initial"
	print graph_queue
	while graph_queue:
		next_node = graph_queue.pop(0)
		for edge in G[next_node] :
			if edge not in visited:
				visited.append(edge)
				print "Visited Node: " + str(edge)
				graph_queue.append(edge)
					
					
					


bfs({1:[2,3] , 2:[1,3,4,5] , 3:[1,2,4] , 4:[2,3] , 5:[2]} , 1)