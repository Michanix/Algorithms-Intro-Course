from random import choice
from math import sqrt

graph = {'A': [1, 2],
         'B': [4, 6],
         'C': [3, 4],
         'D': [3, 2],
         'E': [1, 2]
         }

# euclidean dist
def calc_euclid_distance(p1, p2):
    # finding distance between two points
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# manhattan dist
def calc_manhatan_distance(p1, p2):
    return abs((p1[0] - p2[0]) + (p1[1] - p2[1]))

def total_dist(points):
    # sum of all points in list
    s = 0
    for i, v in enumerate(points[:-1]):
        s += calc_distance(v, points[i+1])
    return s

def main(graph):
    visited = []
    dist = []
    # start edge is random
    u = choice(list(graph.keys()))
    while len(visited) != len(graph):
        # mark as visited
        visited.append(u)
        for k in graph:
            if k not in visited:
                # calculating distance between current edge
                # and next edge
                d = calc_manhatan_distance(graph[u], graph[k])
                dist.append([d, k])
        if len(dist) == 0:
            break
        v = min(dist)[1]
        u = v
        dist.clear()
    return visited
print(main(graph))