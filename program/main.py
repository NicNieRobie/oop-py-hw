# -------------------------------- main.py --------------------------------
#  Program entry point and error messages.
# -------------------------------------------------------------------------

import time
import sys

from container import *
from generate_test import *
import runtime_metrics


# ---------------------------------------------------------------------
# Generates a given amount of files with test cases in given directory.
def generate_test_files(file_count, dir_path):
    for i in range(file_count):
        file_path = dir_path + "/test" + str(i + 1) + ".txt"
        ofstream = open(file_path, "w")
        generate_test(ofstream)
        ofstream.close()
        print("Test generated in", file_path)


# ---------------------------------------------------------------------
# Prints the argument number error.
def arg_num_error():
    print("Incorrect number of arguments in the command line!\n"
          "  Expected:\n"
          "     processname -f infile outfile\n"
          "  Or:\n"
          "     processname -n number outfile\n"
          "  Or:\n"
          "     processname -g number dirpath")


# ---------------------------------------------------------------------
# Prints the input mode error.
def input_mode_error():
    print("Incorrect input mode!\n"
          "  Expected:\n"
          "     processname -f infile outfile\n"
          "  Or:\n"
          "     processname -n number outfile\n"
          "  Or:\n"
          "     processname -g number dirpath")


# ---------------------------------------------------------------------
# Program entry point.
if __name__ == '__main__':
    runtime_metrics.start_time = time.time()
    print("Start")

    # Processing input data.
    if len(sys.argv) != 4:
        arg_num_error()
        runtime_metrics.print_runtime_duration()
        sys.exit(1)

    container = Container()

    if sys.argv[1] == '-f':
        # Reading from file.
        try:
            ifstream = open(sys.argv[2])
        except IOError:
            print("ERROR: Could not open input file!")
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        read_successful = container.read_data(ifstream)

        if not read_successful:
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        ifstream.close()
    elif sys.argv[1] == '-n':
        # Generating container content randomly.
        if not sys.argv[2].isdigit():
            print("ERROR: Invalid container size!")
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        size = int(sys.argv[2])

        if size < 1 or size > 10000:
            print("Amount exceeds the max container size or is non-positive.\n"
                  "Enter a value: 0 < value <= 10000")
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        container.generate_randomly(size)
    elif sys.argv[1] == '-g':
        # Generating tests.
        if not sys.argv[2].isdigit():
            print("ERROR: Invalid file amount!")
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        file_count = int(sys.argv[2])

        if file_count > 100:
            print("ERROR: Number of files is too big, "
                  "please specify an number that is less than 100")
            runtime_metrics.print_runtime_duration()
            sys.exit(1)

        generate_test_files(file_count, sys.argv[3])

        print(file_count, "tests generated at", sys.argv[3])
        runtime_metrics.print_runtime_duration()
        sys.exit(0)
    else:
        input_mode_error()
        runtime_metrics.print_runtime_duration()
        sys.exit(1)

    try:
        ofstream = open(sys.argv[3], "w")
    except IOError:
        print("ERROR: Could not open output file!")
        runtime_metrics.print_runtime_duration()
        sys.exit(1)

    # Printing the results.
    container.print_to_file(ofstream)
    container.print_to_console()

    container.delete_less_than_average()

    ofstream.write('\n\nAfter the function call:\n')
    print('\n\nAfter the function call:')
    container.print_to_file(ofstream)
    container.print_to_console()

    ofstream.close()

    runtime_metrics.print_runtime_duration()