import random

finalcut=1000
with open('kargerMinCut.txt') as f:
    graph = {}
    for line in f:
        line = line.split()
        graph[line[0]] = line[1:]	



def karger_run(data):
	while len(data) > 2:
		#print data
		#1 pick an edge(u,v) uniformly at random , here we make use of python's random module
		u = random.choice(data.keys())
		#print "First Choice: " + str(u) # this line picks a row (minus one for indexing purposes)
		v = random.choice(data[u])# this line picks a column
		#print "Second Choice: " + str(v)	
		#2 merge u and v into a single loop ,removing itself from the indexes
		# merge them into a new node with the index of the smallest between the two , so if u=3 and v = 40 the new node will be 3 
		data[u] = data[u] + data[v]
		data.pop( v , None )# Destroy v 
	
		for key in data:
			data[key] = [u if x==v else x for x in data[key]]

	
		for item in data[u][:]:
			if item==u:
				data[u].remove(item)
			#print "Cleaned self-loops "
	#print data
	#for key in data:
		#print "Length: " + str(len(data[key]))
	#4 return 2 lef:t vertices
	return len(data[data.keys()[0]])

def update(a,b):
	return min(a,b)
		

for iterator in range(10000000):
	karger = karger_run(graph)
	finalcut = update(finalcut , karger)
	
	
print finalcut