# ----------------------------- transport.py ------------------------------
#  Generalized transport data type.
# -------------------------------------------------------------------------

# ---------------------------- type definition ----------------------------
class Transport:
    # Class constructor.
    def __init__(self):
        self.speed = 0
        self.dest_distance = 0

    # ------------------------ type functionality -------------------------

    # Reads data from specified array of strings of certain format and
    #   translates it into a transport class object.
    # param: data_array - array of digits in strings.
    def read_data(self, data_array):
        pass

    # ------------------------------------------------------------------
    # Prints the object's description to the console (standard
    #   output stream).
    def print_to_console(self):
        pass

    # ------------------------------------------------------------------
    # Prints the object's description to given output file stream.
    # param: ofstream - output file stream.
    def print_to_file(self, ofstream):
        pass

    # ------------------------------------------------------------------
    # Returns the time needed for transport to reach its destination.
    def time_to_dest(self):
        return self.dest_distance / self.speed
