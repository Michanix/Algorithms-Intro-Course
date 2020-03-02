from math import sqrt
from itertools import permutations

graph = {'A': [1, 2],
         'B': [4, 6],
         'C': [3, 4],
         'E': [0, 1],
         'D': [4, 3]
         }

# euclidean
def calc_distance(p1, p2):
    # finding distance between two points
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# manhattan dist
def calc_manhatan_distance(p1, p2):
    return abs((p1[0] - p2[0]) + (p1[1] - p2[1]))

def total_dist(points):
    # sum of all points in list
    s = 0
    for i, v in enumerate(points[:-1]):
        s += calc_manhatan_distance(v, points[i+1])
    return s

def main(graph):
    # dict of paths and their distances
    dict_of_paths = {}
    # extracting keys into list
    # to later get list of permutations of keys
    list_of_keys = list(graph.keys())
    # creating all possible paths
    paths = [p for p in permutations(list_of_keys)]
    for i in paths:
        # creating list of points for each permutation(path)
        # [[ ], [ ], [ ]...[ ]]
        points = [graph[j] for j in i]
        # calculating total distance of each
        # created list of points
        d = total_dist(points)
        # creating dictionary of points and they vertices
        # to avoid duplicated value must validate d
        if d not in dict_of_paths.values():
            dict_of_paths[i] = d        

    # print shortest path
    print(min(dict_of_paths, key=dict_of_paths.get))
main(graph)