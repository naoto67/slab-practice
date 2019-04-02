import os
import sys

filename = sys.argv[1]

if not os.path.isfile(filename):
  exit

new_filename = filename.split('.')[0] + '.csv'

os.rename(filename, new_filename)
