import sys
import ipdb

args = sys.argv

if len(args) != 4:
    print("arguments must be 4 pieces")

file_list_name = args[1]
prefix = args[2]
outfile_name = args[3]

try:
    filelist = open(file_list_name, "r")
    outfile = open(outfile_name, "w")

    lines = filelist.readlines()

    for i, line in enumerate(lines):
        serial = '_{:0>3}_'.format(i)
        new_filename = prefix + serial + line.split('_')[-1]
        outfile.write(new_filename)

    filelist.close()
    outfile.close()
except Exception as e:
    print(e)
