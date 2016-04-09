import matplotlib
import res
import spatial


def get_point(split):
    return split[0], spatial.Point(int(split[1]), int(split[2]))

file_restaurant = open(res.file_restaurant, 'r')
restaurant_lines = [line[:-1] for line in file_restaurant]

restaurant_position = [get_point(line.split(',')) for line in restaurant_lines]

for i in restaurant_position:
    print i[0], i[1]