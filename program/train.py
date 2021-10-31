# ------------------------------- train.py --------------------------------
#  Train data type.
# -------------------------------------------------------------------------

from transport import *
from random import randint


# ---------------------------- type definition ----------------------------
class Train(Transport):
    # Class constructor.
    def __init__(self):
        super().__init__()
        self.car_amount = 0

    # ------------------------ type functionality -------------------------

    # Reads data from specified array of strings of certain format and
    #   translates it into a train class object.
    # param: data_array - array of digits in strings.
    def read_data(self, data_array):
        if len(data_array) != 3:
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

        self.speed = int(data_array[0])
        self.dest_distance = float(data_array[1])
        self.car_amount = int(data_array[2])

        return True

    # ------------------------------------------------------------------
    # Prints the object's description to the console (standard
    #   output stream).
    def print_to_console(self):
        print("This is a train. Speed: {}, "
              "distance to destination: {}, "
              "time to distance: {:.2f}, "
              "car amount: {}".format(self.speed, self.dest_distance,
                                      self.time_to_dest(), self.car_amount))

    # ------------------------------------------------------------------
    # Prints the object's description to given output file stream.
    # param: ofstream - output file stream.
    def print_to_file(self, ofstream):
        ofstream.write("This is a train. Speed: {}, "
                       "distance to destination: {}, "
                       "time to distance: {:.2f}, "
                       "car amount: {}\n".format(self.speed, self.dest_distance,
                                                 self.time_to_dest(), self.car_amount))

    # ------------------------------------------------------------------
    # Generates the object's parameters randomly and returns the object.
    def generate_randomly(self):
        self.speed = randint(1, 200)
        self.dest_distance = randint(5, 2000)
        self.car_amount = randint(5, 2000)

        return self
