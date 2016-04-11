import matplotlib.pyplot as plt
import res
import spatial
import random
import heapq


def get_point(split):
    return spatial.Point(int(split[1]), int(split[2]))


def mark_circle(point, color='b', rad=0.3):
    x, y = point.x, point.y
    circle = plt.Circle((x, y), radius=rad, color=color)
    fig.gca().add_artist(circle)

file_restaurant = open(res.file_restaurant, 'r')
restaurant_lines = [line[:-1] for line in file_restaurant]
restaurant_position = [get_point(line.split(',')) for line in restaurant_lines]

file_customer = open(res.file_customer, 'r')
customer_lines = [line[:-1] for line in file_customer]
customer_position = [get_point(line.split(',')) for line in customer_lines]

fig = plt.figure()

rand_index = random.randint(0, len(restaurant_position)-1)
rand_index = 17
query_point = restaurant_position[rand_index]
for restaurant in restaurant_position:
    mark_circle(restaurant, 'magenta')

mark_circle(query_point, color='r', rad=0.5)
plt.text(query_point.x, query_point.y, 'query')

for customer in customer_position:
    mark_circle(customer)

r = 2
customer_list = list()
for customer in customer_position:
    ax = [spatial.get_distance(customer, restaurant) for restaurant in restaurant_position]
    rfn = heapq.nlargest(r, ax)
    rfn = [ax.index(val) for val in rfn]
    print rand_index, rfn
    if rand_index in rfn:
        customer_list.append(customer)

# k = 2
# ax = [spatial.get_distance(query_point, point) for point in customer_list]
# kfn = heapq.nlargest(k, ax)
# kfn = [customer_list[ax.index(dist)] for dist in kfn]

x_point = [[query_point.x, pos.x] for pos in customer_list]
y_point = [[query_point.y, pos.y] for pos in customer_list]

for segment_x, segment_y in zip(x_point, y_point):
    plt.plot(segment_x, segment_y, color='gold')

# dist = [spatial.get_distance(query_point, customer) for customer in customer_position]
# ax = heapq.nlargest(k, dist)
# kfn = [customer_position[dist.index(val)] for val in ax]
#
# x_point = [[query_point.x, pos.x] for pos in kfn]
# y_point = [[query_point.y, pos.y] for pos in kfn]
#
# for segment_x, segment_y in zip(x_point, y_point):
#     plt.plot(segment_x, segment_y, color='magenta')


plt.axis([0, 100, 0, 100])
# plt.axis([0, 20, 0, 15])
plt.show()
