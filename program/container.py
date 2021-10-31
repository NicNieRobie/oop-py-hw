# ----------------------------- container.py ------------------------------
#  Basic data type acting as a container for the transport data type.
# -------------------------------------------------------------------------

from transport_package import *
from random import randint


# ---------------------------- type definition ----------------------------
class Container:
    # Class constructor.
    def __init__(self):
        self.data = []

    # ------------------------ type functionality -------------------------

    # Reads data from input file stream and fills the container with
    #   objects generated from data.
    # param: ifstream - input file stream.
    def read_data(self, ifstream):
        file_data = ifstream.read()

        string_data_arr = file_data.split("\n")

        for string_data in string_data_arr:
            transport_data = string_data.split(" ")
            transport_type = int(transport_data[0])

            if transport_type == 1:
                transport = Plane()
            elif transport_type == 2:
                transport = Ship()
            elif transport_type == 3:
                transport = Train()
            else:
                print("ERROR: Incorrect transport type identifier")
                return False

            read_successful = transport.read_data(string_data.split(" ")[1:])

            if read_successful:
                self.data.append(transport)
            else:
                print("Could not read values - please check input for validity")
                return False

        return True

    # ------------------------------------------------------------------
    # Fills the container with given amount of randomly generated
    #   transport objects.
    # param: count - amount of objects to be generated.
    def generate_randomly(self, count):
        for i in range(count):
            transport_type = randint(1, 3)

            if transport_type == 1:
                transport = Plane()
            elif transport_type == 2:
                transport = Ship()
            else:
                transport = Train()

            self.data.append(transport.generate_randomly())

    # ------------------------------------------------------------------
    # Prints the container data to console (standard output stream).
    def print_to_console(self):
        print("Container contains", len(self.data), "elements.")

        for i in range(len(self.data)):
            print(i + 1, ":", sep="", end=" ")
            self.data[i].print_to_console()

    # ------------------------------------------------------------------
    # Prints the container data to output file stream.
    # param: ofstream - output file stream.
    def print_to_file(self, ofstream):
        ofstream.write("Container contains " + str(len(self.data)) + " elements.\n")

        for i in range(len(self.data)):
            ofstream.write(str(i + 1) + ": ")
            self.data[i].print_to_file(ofstream)

    # ------------------------------------------------------------------
    # Deletes all items with a time_to_dest value less than average
    #   from container.
    def delete_less_than_average(self):
        param_sum = 0

        for transport in self.data:
            param_sum += transport.time_to_dest()

        avg = param_sum / len(self.data)

        for transport in self.data:
            if transport.time_to_dest() < avg:
                self.data.remove(transport)
