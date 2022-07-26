import sys

fname = sys.argv[1]

print('fname', fname)

lines = open(fname).readlines()
print('lines', len(lines))


curr_tx = 0
marf_reads_this_tx = 0
for line in lines:
    if "MarfConnection::get" in line:
        marf_reads_this_tx += 1
        pass
    elif "build_anchored_block delta" in line:
        pass
    elif "candidate delta tx" in line:
        time_parts = line.split('time_cost=')
        if len(time_parts) > 1:
            time_part = time_parts[1]
            print('curr_tx', curr_tx, 'marf_reads_this_tx', marf_reads_this_tx, 'time_part', time_part)
        else:
            print('error on line:', line)

        # Do after printing
        marf_reads_this_tx = 0
        curr_tx += 1

        pass
    else:
        print('line not recognized:', line)
