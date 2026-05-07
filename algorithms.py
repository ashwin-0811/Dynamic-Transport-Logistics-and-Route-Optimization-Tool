import numpy as np


class Algorithms:
    def nearest_neighbor(self, obj, start):
        if start not in obj.locations:
            return [], 0

        unvisited = list(obj.locations)
        unvisited.remove(start)
        route, total_dist, current = [start], 0, start

        while unvisited:
            # Find the closest city from current that hasn't been visited
            dists = obj.distances.loc[current, unvisited]
            nearest_city = dists.idxmin()
            dist_value = dists.min()

            if dist_value == np.inf: break

            total_dist += dist_value
            route.append(nearest_city)
            unvisited.remove(nearest_city)
            current = nearest_city

        return route, total_dist