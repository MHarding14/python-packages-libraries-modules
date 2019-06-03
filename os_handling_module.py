# Modules
    # We have been creating and importing modules
    # Modules abstract functionality

import os

working_dir = os.getcwd()
print(working_dir)

def return_logged_in_user():
    return os.getlogin()

def encode_file(filename):
    return os.fsencode(filename)

def decode_file(filename):
    return os.fsdecode(filename)