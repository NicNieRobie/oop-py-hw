# --------------------------- generate_test.py ----------------------------
#  Contains a function for generating a test input case.
# -------------------------------------------------------------------------

from random import randint


# Function that generates and writes a test input case to output file stream.
def generate_test(ofstream):
    entity_count = randint(5, 20)

    while entity_count > 0:
        transport_type = randint(1, 3)
        speed = randint(100, 700)
        dist_to_dest = randint(500, 3000)

        ofstream.write("{} {} {} ".format(transport_type, speed, dist_to_dest))

        line_end = "" if entity_count == 1 else '\n'

        if transport_type == 1:
            max_reach = randint(500, 7000)
            cap = randint(3, 300)
            ofstream.write("{} {}".format(max_reach, cap) + line_end)
        elif transport_type == 2:
            ship_type = randint(1, 3)
            disp = randint(1000, 15000)
            ofstream.write("{} {}".format(ship_type, disp) + line_end)
        else:
            car_amount = randint(5, 15)
            ofstream.write("{}".format(car_amount) + line_end)

        entity_count -= 1
