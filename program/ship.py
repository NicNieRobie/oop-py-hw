# -------------------------------- ship.py --------------------------------
#  Ship data type.
# -------------------------------------------------------------------------

from transport import *
from random import randint


# ---------------------------- type definition ----------------------------
class Ship(Transport):
    # Ship types dictionary.
    SHIP_TYPES = {
        1: "liner",
        2: "tugboat",
        3: "tanker"
    }

    # Class constructor.
    def __init__(self):
        super().__init__()
        self.ship_type = 0
        self.displacement = 0

    # ------------------------ type functionality -------------------------

    # Reads data from specified array of strings of certain format and
    #   translates it into a ship class object.
    # param: data_array - array of digits in strings.
    def read_data(self, data_array):
        if len(data_array) != 4:
            return False

        for value in data_array:
            if not value.isdigit():
                print("ERROR: Non-number value "
                      "detected while reading input")
                return False

            if int(value) < 0:
                print("ERROR: Negative parameter value "
                      "detected while reading input")
                return False

        if not 1 <= int(data_array[2]) <= 3:
            print("ERROR: Invalid ship type value")
            return False

        self.speed = int(data_array[0])
        self.dest_distance = float(data_array[1])
        self.ship_type = int(data_array[2])
        self.displacement = int(data_array[3])

        return True

    # ------------------------------------------------------------------
    # Prints the object's description to the console (standard
    #   output stream).
    def print_to_console(self):
        ship_type_str = Ship.SHIP_TYPES[self.ship_type]

        print("This is a ship. Speed: {}, "
              "distance to destination: {}, "
              "time to distance: {:.2f}, ship type: {}, "
              "displacement: {}".format(self.speed, self.dest_distance,
                                        self.time_to_dest(), ship_type_str,
                                        self.displacement))

    # ------------------------------------------------------------------
    # Prints the object's description to given output file stream.
    # param: ofstream - output file stream.
    def print_to_file(self, ofstream):
        ship_type_str = Ship.SHIP_TYPES[self.ship_type]

        ofstream.write("This is a ship. Speed: {}, "
                       "distance to destination: {}, "
                       "time to distance: {:.2f}, ship type: {}, "
                       "displacement: {}\n".format(self.speed, self.dest_distance,
                                                   self.time_to_dest(), ship_type_str,
                                                   self.displacement))

    # ------------------------------------------------------------------
    # Generates the object's parameters randomly and returns the object.
    def generate_randomly(self):
        self.speed = randint(1, 200)
        self.dest_distance = randint(5, 2000)
        self.ship_type = randint(1, 3)
        self.displacement = randint(1000, 65000)

        return self
