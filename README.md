Playing Sea of Thieves,my friends and I found a need to build routes to visit several points on map. Instead of looking for them on the map and figuring out which way would be the fastest, we decided to automate that.

This script takes as an input the ship's current coordinates (specifically, coordinates mean the quadrant on the map) and all the points one needs to visit, then figures out all possible paths\* and calculates approximate distances of them, choosing the shortest one. 

\* (It's inefficient, but in reality one rarely needs to visit more than 5-6 points, which is 6! paths. Plus, half of those paths are inverses of the other half, so we can cut down computations in half.

Bonus: since one needs to input point names manually, there is a typos correction mechanism of sorts in-built. 

