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
    #Add a 0 at the end so there is always a left_total and a right_total
    #Since [-1] accesses the last element in the list, there is no need to
    #add a guard at the head of the list
    previous_totals.append(0)

    #Iterate over each level in the graph
    for level_index in xrange(1, len(graph)):
        #Need to keep track of the best totals for this level
        current_totals = []

        current_level = graph[level_index]
        for node_index in xrange(len(current_level)):
            #Work out the parent totals of this node
            left_total = previous_totals[node_index]
            right_total = previous_totals[node_index - 1]
            #Whichever parent has a bigger total sum is the best path to this node
            current_total = max(left_total, right_total) + current_level[node_index]
            #Keep track of that for use next level
            current_totals.append(current_total)
        #Now we can move to the next level
        #Therefore the current_totals become the previous_totals
        previous_totals = current_totals
        #Add the guard 0 (see above)
        previous_totals.append(0)
    #The final totals (now in previous_totals) are the most expensive total to
    #each final node. Therefore, the highest of these is the most expensive
    #route overall
    return max(previous_totals)

GRAPHS = [
    load_graph('./graphs/0.txt'),
    load_graph('./graphs/1.txt'),
    load_graph('./graphs/2.txt'),
    load_graph('./graphs/3.txt'),
    load_graph('./graphs/4.txt'),
    load_graph('./graphs/5.txt'),
    load_graph('./graphs/6.txt'),
    load_graph('./graphs/7.txt'),
    load_graph('./graphs/8.txt'),
    load_graph('./graphs/9.txt'),
]

def check_all():
    results = []
    for graph in GRAPHS:
        results.append(solve_graph(graph))
    return results

def test_time(outer_count=5, inner_count=300):
    import time
    print '\n\nTook (time.time):\n'
    for outer in xrange(outer_count):
        start_time = time.time()
        for inner in xrange(inner_count):
            check_all()
        end_time = time.time()
        diff_time = end_time - start_time
        print '%.2fs' % diff_time

def test_clock(outer_count=5, inner_count=300):
    import time
    print '\n\nTook (time.clock):\n'
    for outer in xrange(outer_count):
        start_time = time.clock()
        for inner in xrange(inner_count):
            check_all()
        end_time = time.clock()
        diff_time = end_time - start_time
        print '%.2fs' % diff_time

def test_timeit(outer_count=5, inner_count=300):
    import timeit
    print '\n\nTook (timeit):\n'
    for outer in xrange(outer_count):
        diff_time = timeit.timeit(check_all, number=inner_count)
        print '%.2fs' % diff_time

#print check_all()
test_time()
test_clock()
test_timeit()
