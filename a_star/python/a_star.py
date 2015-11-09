###########################################################################################################################
#IMPLEMENTATION OF A* SEARCH on a weighted, directed graph.
#heuristic parameter is the name of the admissible function a_star is going to call every time it requires the heuristic value from a particular node to the target node
	#example: heuristic ('K', 'Z') = 10 if the heuristic value from node 'K' to target node 'Z' = 10
#NOTE: heuristic (target) must return 0, since distance between target & itself is always 0
###########################################################################################################################

from heapq import heapify, heappush, heappop;

def a_star (graph, start, end, heuristic):
	current = (heuristic (start, end), start);
	queue, path, length, backtrace = [current], [], 0, {start : (None, 0)};

	heapify (queue);
	while (not current [1] == end):
		try:
			current = heappop (queue);
		except Exception as e:
			return ( (-1, []) );

		for node in graph [current [1]]:
			backtrace [node [0]] = (current [1], node [1]);
			heappush (queue, (current [0] + node [1] + heuristic (node [0], end) - heuristic (current [1], end), node [0]));

	while (end):
		path = [end] + path;
		end, length = backtrace [end] [0], length + backtrace [end] [1];

	return ( (length, path) );

#EXAMPLE OF HEURISTIC FUNCTION
def heuristic (current, target):
	#this heuristic function simply assumes that the target is F, just for simplicity's sake. The heuristic values are made up, but are at most equal to the shortest path, i.e., never overestimate the cost (being admissible implies that)
	estimates = {
		'A': 7,
		'B': 2,
		'C': 4,
		'D': 7,
		'E': 3,
		'F': 0
	};
	return (estimates [current]);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a set of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3.
graph = {
	'A': set ([ ('C', 4), ('D', 3), ('E', 8) ]),
	'B': set ([ ('C', 4), ('F', 2) ]),
	'C': set ([ ('E', 1), ('F', 5) ]),
	'D': set ([ ('B', 6) ]),
	'E': set ([ ('F', 3) ]),
	'F': set ([])
};

#SAMPLE CALL TO THE FUNCTION
print (a_star (graph, 'A', 'F', heuristic));
