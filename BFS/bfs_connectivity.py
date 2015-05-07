

def bfs(G , S):# graph = G , start_vertex = s , supose G is a dictionary
	graph_queue = [S]
	visited = []
	print "Graph Queue initial"
	print graph_queue
	while graph_queue:
		next_node = graph_queue.pop(0)
		if next_node not in visited:
			visited.append(next_node)
		for edge in G[next_node] :
			if edge not in visited:
				visited.append(edge)
				print "Visited Node: " + str(edge)
				graph_queue.append(edge)
	return visited

def graph_connectivity( G , visited=[] ):
	i=0
	for node in G:
		if node not in visited:
			i+=1
			visited+= bfs( G , node )
			print str(i)+'-th subgraph'
			print visited
	return visited
#graph = {1:[2,3] , 2:[1,3,4,5] , 3:[1,2,4] , 4:[2,3] , 5:[2,6] , 6:[5] , 7:[] , 8:[]}
graph_connectivity(graph)


		