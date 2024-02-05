graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

def has_path(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        curr_node = queue.pop()
        if curr_node == dst:
            return True

        for neighbor in graph[curr_node]:
            queue.insert(0, neighbor)

    return False