import sys

fname = sys.argv[1]

print('fname', fname)

lines = open(fname).readlines()
print('lines', len(lines))


for line in lines:
    if "MarfConnection::get" in line:
        pass
    elif "build_anchored_block delta" in line:
        pass
    elif "candidate delta tx" in line:
        pass
    else:
        print('line not recognized:', line)
