# finding solutions for convexhull problem
# by implementing Graham`s scan algorithm

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from random import randint
from math import atan2, degrees


def top(stack):
    return stack[-1]

def next_to_top(stack):
    return stack[-2]

def leftmost_point(points):
    # returns the point with
    # leftmost Y value
    return min(points, key=lambda y: y[1])

def get_polar_coords(p1, p2):
    # find polar coords
    v = (p2[0]-p1[0], p2[1]-p1[1])
    r = (v[0]**2 + v[1]**2)**0.5
    angl = degrees(atan2(v[1], v[0]))
    return r, angl

def get_cross_prod(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def plot_results(ch_p, points):
    # ch_p -> convex hull points
    # points -> original points
    n = len(ch_p)
    xi = [x[0] for x in points]
    yi = [y[1] for y in points]
    codes = [Path.MOVETO] + [Path.LINETO]*(n-1)
    path = Path(ch_p, codes)
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor='none', lw=2)
    ax.scatter(xi, yi)  # plotting the original points
    ax.add_patch(patch) # applying patch to draw borders
    ax.set_xlim(-1, max(xi) + 1) # adjusting x, y limits for more beuty
    ax.set_ylim(-1, max(yi) + 1)
    plt.grid(True)
    plt.show()
    
def graham_scan(points):
    S = []
    p0 = leftmost_point(points)
    # calculate polar coords with respect to p0
    polar_coords = [get_polar_coords(p0, p) for p in points if p != p0]
    # sort the by polar angle in counterclockwise order
    sorted_coords = sorted([p for p in points if p != p0], key=lambda p: get_polar_coords(p0, p)[1])
    S.append(p0)
    S.append(sorted_coords[0])
    S.append(sorted_coords[1])
    for i in range(2, len(sorted_coords)):
        while True:
            if len(S) < 2:
                break
            # a = next to top
            # b = top
            # c = p0
            u = (top(S)[0] - next_to_top(S)[0], top(S)[1] - next_to_top(S)[1])
            v = (sorted_coords[i][0] - top(S)[0], sorted_coords[i][1] - top(S)[1])
            if u == v:
                S.pop()
            d = get_cross_prod(u, v)
            if d >= 0:
                break
            else:
                S.pop()
        S.append(sorted_coords[i])
    return S

# point represented as tuple(x, y)
# points represented as list of tuples
points = [(i, randint(0, 9)) for i in range(1, 16)]

conveh_hull = graham_scan(points)
print('Conveh hull = {}'.format(conveh_hull))

# plot the solution
# pass convex hull points and original points
plot_results(conveh_hull, points)
