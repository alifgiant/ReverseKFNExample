import sys
import random

if __name__ == "__main__":
    # input user
    file_address = 'input_restaurant.csv'
    # total city
    n_cities = 100

    # get args from caller
    if len(sys.argv) > 1:
        n_cities = int(sys.argv[1])
    if len(sys.argv) > 2:
        file_address = sys.argv[2]

    file_out = open(file_address, 'w')

    cartesian_distance = n_cities*2

    random_seed_x = range(cartesian_distance)
    random.shuffle(random_seed_x)

    for i in xrange(n_cities):
        file_out.write(str(i)+','+str(random_seed_x[i])+','+str(random.randint(0, cartesian_distance))+'\n')

