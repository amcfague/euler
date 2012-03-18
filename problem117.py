import gmpy

ROW_LENGTH = 50
RED_LENGTH = 2
GREEN_LENGTH = 3
BLUE_LENGTH = 4

ALL_COLORS = [BLUE_LENGTH, GREEN_LENGTH, RED_LENGTH]


def get_number_combinations(num_tiles=0, accum_tile_length=0, row_length=ROW_LENGTH):
    if accum_tile_length > row_length:
        return 0

    total_tiles = num_tiles + row_length - accum_tile_length
    s = gmpy.comb(total_tiles, num_tiles)
    for color_tile_length in ALL_COLORS:
        s += get_number_combinations(num_tiles + 1, accum_tile_length +
                                     color_tile_length)
    return s

print get_number_combinations()
