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
    import pdb
    #pdb.set_trace()

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
