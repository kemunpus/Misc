import sys
import math
import time
import tkinter as tk


def read_cities():
    cities = []

    for line in sys.stdin:
        values = line.split()
        cities.append((int(values[0]), int(values[1])))

    return cities


def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx*dx+dy*dy)


def calc_path_length(cities, paths):
    path_length = 0

    for i in range(len(paths)-1):
        path_length += calc_distance(paths[i], paths[i+1])

    return path_length


def make_paths_greedy(cities, start_city):
    city_count = len(cities)
    visited = [False] * city_count
    paths = []
    current_city = start_city

    while True:
        paths.append(current_city)
        visited[current_city] = True
        min_distance = 0
        best_city = current_city

        for dest_city in range(city_count):

            if visited[dest_city] == False:
                distance = calc_distance(current_city, dest_city)

                if min_distance == 0 or distance < min_distance:
                    min_distance = distance
                    best_city = dest_city

        if best_city == current_city:
            break

        current_city = best_city

    paths.append(start_city)

    return paths


def two_opt(cities, paths):
    size = len(cities)

    while True:
        count = 0

        for i in range(size - 2):
            i1 = i + 1

            for j in range(i + 2, size):

                if j == size - 1:
                    j1 = 0
                else:
                    j1 = j + 1

                if i != 0 or j1 != 0:
                    l1 = calc_distance(paths[i], paths[i1])
                    l2 = calc_distance(paths[j], paths[j1])
                    l3 = calc_distance(paths[i], paths[j])
                    l4 = calc_distance(paths[i1], paths[j1])

                    if l1 + l2 > l3 + l4:
                        new_paths = paths[i1:j+1]
                        paths[i1:j+1] = new_paths[::-1]
                        count += 1

        if count == 0:
            break

    return paths


def draw_paths(cities, paths, message):
    max_x = 700
    max_y = 600
    scale = 2.5
    city_mark = 12

    root = tk.Tk()
    canvas = tk.Canvas(root, width=max_x, height=max_y, bg="white")
    canvas.pack()

    canvas.create_text(max_x/2, 20, text=message, justify='center')

    for i in range(len(cities)):
        x, y = cities[i]
        city_color = 'red' if i == 0 else 'green'
        canvas.create_oval(x * scale - city_mark,
                           max_y - y * scale - city_mark,
                           x * scale + city_mark,
                           max_y - y * scale + city_mark,
                           fill=city_color)

        canvas.create_text(x * scale, max_y - y * scale,
                           text=str(i), justify='center')

    for i in range(len(paths)-1):
        x1, y1 = cities[paths[i]]
        x2, y2 = cities[paths[i+1]]
        canvas.create_line(x1 * scale, max_y - y1 * scale,
                           x2 * scale, max_y - y2 * scale)

    root.mainloop()


cities = read_cities()
print('cities : {}'.format(cities))

paths = make_paths_greedy(cities, 0)
print('paths : {}'.format(paths))

path_length = calc_path_length(cities, paths)
print('path length : {}'.format(path_length))

opt = True

if opt:
    paths = two_opt(cities, paths)
    print('opt paths : {}'.format(paths))

    path_length = calc_path_length(cities, paths)
    print('opt path length : {}'.format(path_length))

draw_paths(cities, paths, "Path length : {}".format(path_length))
