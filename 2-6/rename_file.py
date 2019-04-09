import sys
import codecs
import ipdb

args = sys.argv

if len(args) != 4:
    print("arguments must be 4 pieces")

file_list_name = args[1]
prefix = args[2]
outfile_name = args[3]

try:
    filelist = codecs.open(file_list_name, "r", 'shift_jis')
    outfile = open(outfile_name, "w")

    lines = filelist.readlines()

    for i, line in enumerate(lines):
        serial_code = '_{:0>3}_'.format(i)
        new_filename = prefix + serial_code + line.split('_')[-1]
        outfile.write(new_filename)
    filelist.close()
    outfile.close()
except Exception as e:
    print(e)
