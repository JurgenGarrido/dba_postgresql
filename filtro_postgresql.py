import re
import sys

arguments = sys.argv

cont_panic = 0
cont_fatal = 0
cont_error = 0
cont_warning = 0

with open(arguments[1], "r") as f:
    for line in f:
        if re.search(r"(PANIC)", line):
            cont_panic += 1
            print(line)
        if re.search(r"(FATAL)", line):
            cont_fatal += 1
            print(line)
        if re.search(r"(ERROR)", line):
            cont_error += 1
            print(line)
        if re.search(r"(WARNING)", line):
            cont_warning += 1
            print(line)

    print("==================================")
    print("WARNING: " + str(cont_warning))
    print("ERROR: " + str(cont_error))
    print("FATAL: " + str(cont_fatal))
    print("PANIC: " + str(cont_panic))
    print("==================================")
    print("TOTAL: " + str(cont_warning + cont_error + cont_fatal + cont_panic))
    print("==================================")



