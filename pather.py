import Levenshtein
import numpy as np
import math
import re
from itertools import permutations


def quadrant_to_coords(quadrant):
    """
	Turns a quadrant identifier to matrix coordinates

	Args:
	  quadrant : string of type letter-number

	Returns:
	  coordinates : tuple of matrix indices corresponding to the quadrant ID
	"""
    coordinates = (ord(quadrant[0]) - 97, int(quadrant[1:]) - 1)
    return coordinates


def find_points_distance(a, b):
    """
    Finds distance between two points (points' coordinates)

    Args:
      a: a tuple of coordinates of the first point
      b: a tuple of coordinates of the second point

    Returns:
      distance between the points :: int
    """
    # Find the difference in coordinates
    diff = (abs(b[0] - a[0]), abs(b[1] - a[1]))
    direct = math.sqrt(diff[0] ** 2 + diff[1] ** 2)
    return direct


def find_path_distance(path):
    """
    Find a total path length by iteratively finding distance between consecutive points
    Args:
      path : list of points(quadrants)

    Returns:
      total distance/path length :: int
    """
    total_distance = sum(map(lambda x: find_points_distance(quadrant_to_coords(x[0]), quadrant_to_coords(x[1])),
                             zip(path, path[1:])))
    total_distance = sum([find_points_distance(quadrant_to_coords(a), quadrant_to_coords(b))
                          for a, b in zip(path, path[1:])])
    return total_distance


while True:
    coords = input('Enter you quadrant: ').casefold()
    if re.match(r"[a-z]([1-9]$|1[0-9]$|2[0-6]$)", coords):
        break
    else:
        print('Quadrant format is "A1".."Z26" (or lowercase)')
ship = coords

sot_map = {'smugglers bay': 'f3',
           'salty sands': 'g3',
           'black sand atol': 'o3',
           'marauders arch': 'q3',
           'sailors bounty': 'c4',
           'picaroon palms': 'i4',
           'scurvy isley': 'k4',
           'old faithful isle': 'm4',
           'the wild treasures store': 'o4',
           'sandy shallows': 'e5',
           'boulder cay': 'g5',
           'shark fin camp': 'p5',
           'black water enclave': 'r5',
           'keel haul fort': 'c6',
           'lone cove': 'h6',
           'kraken watchtower': 'l6',
           'blind mans lagoon': 'n6',
           'plunderers plight': 'q6',
           'the spoils of plenty store': 'b7',
           'sanctuary outpost': 'f7',
           'the sunken grove': 'p7',
           'rapier cay': 'd8',
           'lonely isle': 'g8',
           'hidden spring keep': 'i8',
           'dagger tooth outpost': 'm8',
           'galleons grave outpost': 'r8',
           'crescent isle': 'b9',
           'rum runner isle': 'h9',
           'isle of last words': 'o9',
           'skull keep': 'p9',
           'three paces east seaport': 's9',
           'golden sands outpost': 'd10',
           'cannon cove': 'g10',
           'the north star seapost': 'h10',
           'shipwreck bay': 'm10',
           'tri-rock isle': 'r10',
           'sea dogs rest': 'c11',
           'twin groves': 'h11',
           'the crooked masts': 'o11',
           'shiver retreat': 'q11',
           'liars backbone': 's11',
           'scorched pass': 'x11',
           'molten sands fortress': 'z11',
           'lagoon of whispers': 'd12',
           'wanderers refuge': 'f12',
           'the reapers hideout': 'i12',
           'krakens fall': 'r12',
           'fetchers rest': 'v12',
           'brians bazaar': 'y12',
           'mermaids hideaway': 'b13',
           'shark tooth key': 'p13',
           'cursewater shores': 'y13',
           'sailors knot stronghold': 'e14',
           'fools lagoon': 'i14',
           'castaway isle': 'k14',
           'fort of the damned': 'l14',
           'cinder isle': 'u14',
           'flintlock peninsula': 'w14',
           'barnacle cay': 'o15',
           'plunder valley': 'g16',
           'chicken isle': 'i16',
           'snakes island': 'k16',
           'stephens spoils': 'l16',
           'crooks hollow': 'm16',
           'the forsaken brink': 'u16',
           'discovery ridge': 'e17',
           'the finest trading post': 'f17',
           'lost gold fort': 'h17',
           'paradise spring': 'l17',
           'the crows nest fortress': 'o17',
           'ancient spire outpost': 'q17',
           'morrows peak outpost': 'v17',
           'old salts atoll': 'f18',
           'plunder outpost': 'k18',
           'cutlass cay': 'm18',
           'brimstone rock': 'x18',
           'glowstone cay': 'z18',
           'shark bait cove': 'h19',
           'mutineer rock': 'n19',
           'devils ridge': 'p19',
           'flames end': 'b19',
           'lookout point': 'i20',
           'booty isle': 'k20',
           'thieves haven': 'l20',
           'magmas tide': 'y20',
           'roaring sands': 'u21',
           'the devils thirst': 'w21',
           'ashe reaches': 'v21'}

points = []
while True:
    point = input('Enter destination point. (Leave empty to finish): ').casefold()
    if point == '':
        break
    try:
        quadrant = sot_map[point]
    except KeyError:
        keys = list(sot_map.keys())
        point = keys[np.argmin(list(map(lambda x: Levenshtein.distance(x, point), keys)))]
        quadrant = sot_map[point]
    points.append(quadrant)

paths = []
for p in permutations(points):
    if p[0] <= p[-1]: # Since we don't need inverses
        p = list(p)
        p.insert(0, ship)
        paths.append(p)

best_path = paths[np.argmin([find_path_distance(path) for path in paths])]
print(best_path)
