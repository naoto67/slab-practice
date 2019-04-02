import sys
import ipdb
import os

args = sys.argv

if not (os.path.isfile(args[1]) and os.path.isfile(args[2])):
    exit

ground_file = open(args[1])
result_file = open(args[2])

ground_lines = ground_file.readlines()
result_lines = result_file.readlines()

output = [[0 for i in range(25)] for i in range(25)]

for i, line in enumerate(ground_lines):
    ground_data = int(line.split('\n')[0])
    result_data = int(result_lines[i].split('\n')[0])
    output[ground_data][result_data] += 1

for i in output:
    for j in i:
        print('{:>4}'.format(j), end="")
    print()

ground_file.close()
result_file.close()
