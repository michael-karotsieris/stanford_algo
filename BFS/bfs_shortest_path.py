

def bfs_shortest_path(G , S , V):# graph = G , start_vertex = s , supose G is a dictionary
	graph_queue = [S]
	visited = []
	dist = {}
	dist[S] = 0
	if S != V:
		dist[V] = float( '+inf' )
	print "Graph Queue initial"
	print graph_queue
	while graph_queue:
		next_node = graph_queue.pop(0)
		for edge in G[next_node] :
			if edge not in visited:
				dist[edge] = dist[next_node] + 1
				visited.append(edge)
				print "Visited Node: " + str(edge)
				graph_queue.append(edge)
	return dist[V]				
					
					

print bfs_shortest_path({1:[2,3] , 2:[1,3,4,5] , 3:[1,2,4] , 4:[2,3] , 5:[2,6] , 6:[5] , 7:[]} , 4 , 7)