#!/usr/bin/env python3

#default 2678.08074103

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def greedy(cities):
    N = len(cities)
    sum_dis = 0.0

    dist = [[0] * N for i in range(N)] 
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            
    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        sum_dis += distance(cities[current_city], cities[next_city]) 
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    #print sum_dis + distance(cities[current_city], cities[0]) 
    return solution

def opt_2(path, cities):
    while True:
        count = 0
        for i in range(0, len(path)-2):
            for j in range(i+2, len(path)-1):
                l1 = distance(cities[path[i]], cities[path[i+1]])
                l2 = distance(cities[path[j]], cities[path[j+1]])
                l3 = distance(cities[path[i]], cities[path[j]])
                l4 = distance(cities[path[i+1]], cities[path[j+1]])
                if (l1 + l2) > (l3 + l4):
                    new_path = path[i+1:j+1]
                    path[i+1:j+1] = new_path[::-1] #reverse
                    count += 1 #if not change, finish opt_2.
        if count == 0:
            break
    return path

def solve_distance(path, cities):
    sum_dis = 0
    for i in range(0, len(path)):
        if i == (len(path)-1):
            sum_dis += distance(cities[path[i]], cities[path[0]])
        else:
            sum_dis += distance(cities[path[i]], cities[path[i+1]])
    return sum_dis


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    path= greedy(cities)
    solution = opt_2(path, cities)
    print solve_distance(solution, cities)
    #print_solution(solution)
