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

curr_tx = 0
marf_reads_this_tx = 0
total_marf_time = 0.0
total_processing_time = 0.0
for line in lines:
    marf_key = "MarfConnection::get"
    # marf_key = "MARF::get_by_key"
    if marf_key in line:
        marf_reads_this_tx += 1
        time_part = line.split('time_cost=')[1].split(')')[0]
        parsed = parse_time(time_part)
        total_marf_time += parsed
        pass
    elif "build_anchored_block delta" in line:
        pass
    elif "candidate delta tx" in line:
        time_parts = line.split('time_cost=')
        if len(time_parts) > 1:
            time_part = time_parts[1].strip()
            parsed_time = parse_time(time_part)
            total_processing_time += parsed_time
            marf_fraction = total_marf_time / parsed_time
            print('curr_tx', curr_tx, 'marf_reads_this_tx', marf_reads_this_tx, 'time_part', parsed_time, 'total_marf_time', total_marf_time,
                    'marf_fraction', marf_fraction)
        else:
            # print('error on line:', line)
            pass

        # Do after printing
        curr_tx += 1
        marf_reads_this_tx = 0
        total_marf_time = 0.0

        pass
    else:
        print('line not recognized:', line)

print('total_processing_time', total_processing_time, 'total_marf_time', total_marf_time)
