#!/usr/bin/env python3

language = "Python"
version = 3
pi = 3.14159
computation_valid = version == 3
pi_formatted = "{:.2f}".format(pi)

print("Language: {}".format(language))
print("Version: {}".format(version))
print("Pi approx: " + pi_formatted)
print("Computation valid: {}".format(computation_valid))
