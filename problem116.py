import gmpy

ROW_LENGTH = 50
RED_LENGTH = 2
GREEN_LENGTH = 3
BLUE_LENGTH = 4

def get_number_combinations(tile_length, row_length=ROW_LENGTH):
    s = 0
    for num_tiles in range(1, row_length / tile_length + 1):
        total_tiles = row_length - (num_tiles * tile_length) + num_tiles
        comb = gmpy.comb(total_tiles, num_tiles)
        s += comb
    return s

blue_tiles = get_number_combinations(BLUE_LENGTH)
green_tiles = get_number_combinations(GREEN_LENGTH)
red_tiles = get_number_combinations(RED_LENGTH)

print "Blue:", blue_tiles
print "Green:", green_tiles
print "Red:", red_tiles
print "Total:", blue_tiles + green_tiles + red_tiles
