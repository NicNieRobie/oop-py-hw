# ------------------------------- plane.py --------------------------------
#  Plane data type.
# -------------------------------------------------------------------------

from transport import *
from random import randint


# ---------------------------- type definition ----------------------------
class Plane(Transport):
    # Class constructor.
    def __init__(self):
        super().__init__()
        self.max_distance = 0
        self.capacity = 0

    # ------------------------ type functionality -------------------------

    # Reads data from specified array of strings of certain format and
    #   translates it into a plane class object.
    # param: data_array - array of digits in strings.
    def read_data(self, data_array):
        if len(data_array) != 4:
            return False

        for value in data_array:
            if not value.isdigit():
                print("ERROR: Non-number value detected while reading input")
                return False

            if int(value) < 0:
                print("ERROR: Negative parameter value detected while reading input")
                return False

        self.speed = int(data_array[0])
        self.dest_distance = float(data_array[1])
        self.max_distance = int(data_array[2])
        self.capacity = int(data_array[3])

        return True

    # ------------------------------------------------------------------
    # Prints the object's description to the console (standard
    #   output stream).
    def print_to_console(self):
        print("This is a plane. Speed: {}, "
              "distance to destination: {}, "
              "time to distance: {:.2f}, "
              "maximum flight distance: {}, "
              "capacity: {}".format(self.speed, self.dest_distance,
                                    self.time_to_dest(), self.max_distance, self.capacity))

    # ------------------------------------------------------------------
    # Prints the object's description to given output file stream.
    # param: ofstream - output file stream.
    def print_to_file(self, ofstream):
        ofstream.write("This is a plane. Speed: {}, "
                       "distance to destination: {}, "
                       "time to distance: {:.2f}, "
                       "maximum flight distance: {}, "
                       "capacity: {}\n".format(self.speed, self.dest_distance,
                                               self.time_to_dest(), self.max_distance, self.capacity))

    # ------------------------------------------------------------------
    # Generates the object's parameters randomly and returns the object.
    def generate_randomly(self):
        self.speed = randint(1, 200)
        self.dest_distance = randint(5, 2000)
        self.capacity = randint(100, 300)
        self.max_distance = randint(2000, 4000)

        return self
