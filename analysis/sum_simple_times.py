import sys

fname = sys.argv[1]

print('fname', fname)

lines = open(fname).readlines()
print('lines', len(lines))

def parse_time(time_string):
    number = 0.0
    factor = 0.0
    milli = 0.001
    if time_string.endswith('µs'):
        factor = milli * milli
        number = float(time_string[:-2])
    elif time_string.endswith('ms'):
        factor = milli
        number = float(time_string[:-2])
    elif time_string.endswith('s'):
        factor = 1.0
        number = float(time_string[:-1])
    # print ('time_string', time_string, factor, number)
    return factor * number

s = 0.0
for line in lines:
    time_part = line.strip()
    time = parse_time(time_part)
    s += time

print('s', s)
