
def dfs( G , S , visited=[] ):
	print G
	graph_queue = [S]
	visited = [S]
	while graph_queue:
		next_node = graph_queue.pop(-1)
		print "Next Node: " + str(next_node)
		for edge in G[next_node]:
			if edge not in visited:
				visited.append(edge)
				graph_queue.append(edge)
				print "Visited Edge: " + str(edge)
	print visited		

dfs({1:[2,3] , 2:[1,4] , 3:[1,6] , 4:[2,5] , 5:[4] , 6:[3,7] , 7:[6]} , 1)	