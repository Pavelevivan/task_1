

def merge_trees(names, tree_sizes, next, node_1, node_2):
    name_1 = names[node_1]
    name_2 = names[node_2]
    neibor = next[node_2]
    while names[neibor] != name_1:
        names[neibor] = name_1
        neibor = next[neibor]
    tree_sizes[name_1] = tree_sizes[name_1] + tree_sizes[name_2]
    x = next[node_1]
    y = next[node_2]
    next[node_1] = y
    next[node_2] = x


def build_min_ostov(arr_adjency, edges):
    ostov = []
    names = {}
    tree_sizes = {}
    next = {}
    for x in arr_adjency.keys():
        names[x] = x
        next[x] = x
        tree_sizes[x] = 1
    while len(ostov) != len(arr_adjency.keys()) -1:
        edge = edges.pop(-1)
        node_1 = edge[1][0]
        node_2 = edge[1][1]
        if names[node_1] != names[node_2]:
            if tree_sizes[node_1] > node_2:
                merge_trees(names, tree_sizes, next, node_1, node_2)
            else:
                merge_trees(names, tree_sizes, next, node_2, node_1)
        ostov.append(edge)
    print(ostov)
    return ostov

def get_dict_adj(arr_adjency):
    edges = []
    dict_adj = {}
    for i, start_index in enumerate(arr_adjency):
        if start_index == len(arr_adjency):
            break
        dict_adj[i+1] = {}
        node_dist = arr_adjency[start_index - 1: arr_adjency[i + 1] - 1]
        for j in range(0, len(node_dist), 2):
            node, dist = node_dist[j: j + 2]
            if (dist, (node, i+1)) not in edges:
                edges.append((dist, (i + 1, node)))
            dict_adj[i+1][node] = dist
    edges.sort(reverse=True)
    print(edges)
    print(dict_adj)
    return edges, dict_adj


def parse_input_file(file='in.txt'):
    arr_adjency = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines[1:]:
            arr_line = [int(x) for x in line.split(' ') if x]
            arr_adjency.extend(arr_line)
    print(arr_adjency)
    return arr_adjency


def save_result(min_ostov):
    adj_list = {}
    result = 0
    for edge in min_ostov:
        node_1 = edge[1][0]
        node_2 = edge[1][1]
        result += edge[0]
        if node_2 not in adj_list:
            adj_list[node_2] = []
        if node_1 not in adj_list:
            adj_list[node_1] = []
        adj_list[node_2].append(node_1)
        adj_list[node_1].append(node_2)
    print(adj_list)
    with open('out.txt', 'w') as f:
        for x in sorted(adj_list.keys()):
            line = str(x) + ' '
            for neibor in adj_list[x]:
                line += str(neibor) + ' '
            line += '0\n'
            f.write(line)
        f.write(str(result))


if __name__ == '__main__':
    arr_adjency = parse_input_file()
    edges, dict_adj = get_dict_adj(arr_adjency)
    min_ostov = build_min_ostov(dict_adj, edges)
    save_result(min_ostov)

