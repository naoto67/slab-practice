import os
import sys
import shutil

filename = sys.argv[1]

if not os.path.isfile(filename):
  exit

new_filename = filename.split('.')[0] + '.txt'

# shutil.copy(filename, new_filename)

os.rename(filename, new_filename)
