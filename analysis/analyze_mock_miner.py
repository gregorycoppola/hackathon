import sys

fname = sys.argv[1]

print('fname', fname)

lines = open(fname).readlines()
print('lines', len(lines))

def parse_time(time_string):
    number = 0.0
    factor = 0.0
    milli = 0.001
    if time_string.endswith('ns'):
        factor = milli * milli * milli
        number = float(time_string[:-2])
    elif time_string.endswith('µs'):
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

cutoffs = [0.0, 10.0, 20.0]
for cutoff in cutoffs:
    total_inside = 0.0
    total_outside = 0.0
    for idx, line in enumerate(lines):
        if not "total_inside_time: " in line:
            continue

        inside_part = line.split("total_inside_time: ")[1].split(" ")[0]
        outside_part = line.split("total_outside_time: ")[1].split(" ")[0]

        inside_time = parse_time(inside_part)
        outside_time = parse_time(outside_part)

        total = inside_time + outside_time
        if total >= cutoff:
            total_inside += inside_time
            total_outside += outside_time

    fraction = total_inside / total_outside
    print ('cutoff', cutoff, 'total_inside', total_inside, 'total_outside', total_outside, 'fraction', fraction)

