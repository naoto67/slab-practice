import os
import sys
import ipdb
import shutil

old_filename = sys.argv[1]
if not os.path.isfile(old_filename):
  exit

new_filename = old_filename.split('.')[0] + '.txt'

old_file = open(old_filename, "r")
new_file = open(new_filename, "w")

lines = old_file.readlines()

for line in lines:
    new_file.write(line.replace(',', ' '))

old_file.close()
new_file.close()
