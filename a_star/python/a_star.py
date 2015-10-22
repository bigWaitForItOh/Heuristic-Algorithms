###########################################################################################################################
#IMPLEMENTATION OF A* SEARCH on a weighted, directed graph.
#heuristic parameter is the name of the admissible function a_star is going to call every time it requires the heuristic value from a particular node to the target node
	#example: heuristic ('K', 'Z') = 10 if the heuristic value from node 'K' to target node 'Z' = 10
#NOTE: heuristic (target) must return 0, since distance between target & itself is always 0
###########################################################################################################################

from heapq import heapify, heappush, heappop;

def a_star (graph, start, end, heuristic):
	current = (0, start);
	queue, path, backtrace, length = [current], [], {start : (None, 0)}, 0;

	heapify (queue);
	while (not current [1] == end):
		try:
			current = heappop (queue);
		except Exception as e:
			return (-1, []);

		for next_node in graph [current [1]]:
			heappush (queue, (next_node [1] + heuristic (next_node [0], end), next_node [0]));
			backtrace [next_node [0]] = (current [1], next_node [1]);

	while (not end == None):
		length += backtrace [end] [1];
		path, end = [end] + path, backtrace [end] [0];

	return (length, path);

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
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a set of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3.
graph = {
	'A': set ([ ('B', 2), ('C', 3) ]),
	'B': set ([ ('C', 3), ('D', 5), ('E', 8) ]),
	'C': set ([ ('D', 6) ]),
	'D': set ([ ('E', 8), ('F',6) ]),
	'E': set ([ ('F', 6) ]),
	'F': set ([])
};

#SAMPLE CALL TO THE FUNCTION
print (a_star (graph, 'A', 'F', heuristic));
