def load_graph(path):
    """
    Load an outrun graph from the given file
    Return an array of arrays e.g.
    [
        [1],
        [1,2],
        [1,2,3],
        ...
    ]
    Each node can talk to the node directly below it & the node to the right

    """
    graph = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == '#':
                continue
            nodes = [int(node) for node in line.split(' ')]
            graph.append(nodes)
    return graph

def solve_graph(graph):
    """
    Find the most expensive route through the given graph
    """
    #We need to keep track of the totals for each best path so far
    #Initially, this is just whatever is in the first level of the graph
    previous_totals = graph[0]

    #Iterate over each level in the graph
    for level_index in xrange(1, len(graph)):
        #Need to keep track of the best totals for this level
        current_totals = []

        current_level = graph[level_index]
        for node_index in xrange(len(current_level)):
            #Work out the parents of this node
            left_total = 0
            right_total = 0
            if node_index < len(previous_totals):
                #There is a left_parent
                left_total = previous_totals[node_index]
            if node_index > 0:
                #There is a right_parent
                right_total = previous_totals[node_index - 1]
            #Whichever parent has a bigger total sum is the best path to this node
            current_total = max(left_total, right_total) + current_level[node_index]
            #Keep track of that for use next level
            current_totals.append(current_total)
        #Now we can move to the next level
        #Therefore the current_totals become the previous_totals
        previous_totals = current_totals
    #The final totals (now in previous_totals) are the most expensive total to
    #each final node. Therefore, the highest of these is the most expensive
    #route overall
    return max(previous_totals)

def check_all():
    print solve_graph(load_graph('./graphs/0.txt'))
    print solve_graph(load_graph('./graphs/1.txt'))
    print solve_graph(load_graph('./graphs/2.txt'))
    print solve_graph(load_graph('./graphs/3.txt'))
    print solve_graph(load_graph('./graphs/4.txt'))
    print solve_graph(load_graph('./graphs/5.txt'))
    print solve_graph(load_graph('./graphs/6.txt'))
    print solve_graph(load_graph('./graphs/7.txt'))
    print solve_graph(load_graph('./graphs/8.txt'))
    print solve_graph(load_graph('./graphs/9.txt'))

check_all()
