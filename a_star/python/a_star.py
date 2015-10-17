###########################################################################################################################
#IMPLEMENTATION OF A* SEARCH on a weighted, directed graph.
#heuristic parameter is the name of the admissible function a_star is going to call every time it requires the heuristic value from a particular node to the target node
	#example: heuristic ('K', 'Z') = 10 if the heuristic value from node 'K' to target node 'Z' = 10
#NOTE: heuristic (target) must return 0, since distance between target & itself is always 0
###########################################################################################################################

from heapq import heapify, heappush, heappop;

def a_star (graph, source, target, heuristic):
	current_node = (0, source, [source]);
	queue = [current_node];

	heapify (queue);
	while (not current_node [1] == target):
		try:
			current_node = heappop (queue);
		except Exception as e:
			return (-1, []);

		for neighbour in graph [current_node [1]]:
			heappush (queue, (neighbour [1] + heuristic (neighbour [0], target), neighbour [0], current_node [2] + [neighbour [0]]));

	return (current_node [0], current_node [2]);

#EXAMPLE OF HEURISTIC FUNCTION
def heuristic (current, target):
	#this heuristic function simply assumes that the target is F, just for simplicity's sake. The heuristic values are made up, but are at most equal to the shortest path, i.e., never overestimate the cost (being admissible implies that)
	estimates = {
		'A': 13,
		'B': 9,
		'C': 12,
		'D': 4,
		'E': 5,
		'F': 0
	};
	return (estimates [current]);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a list of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3.
graph = {
	'A': [ ('B', 2), ('C', 3) ],
	'B': [ ('C', 3), ('D', 5), ('E', 8) ],
	'C': [ ('D', 6) ],
	'D': [ ('E', 8), ('F',6) ],
	'E': [ ('F', 6) ],
	'F': []
};

#SAMPLE CALL TO THE FUNCTION
print (a_star (graph, 'A', 'F', heuristic));