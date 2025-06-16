# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

directoyPath = "/"

currentdirlist = os.listdir(directoyPath)

for entry in currentdirlist :
    print(entry)