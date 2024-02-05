graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

def has_path(graph, src, dst):
    if src == dst: return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True

    return False

