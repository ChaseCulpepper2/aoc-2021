# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6#part2

import os

def solve_part_one(file='../solutions/inputs/8.in'):
    sys_states = load_file(file)

    num_1478 = sum([len([x for x in sys_state['outputs'] if len(x) in [2, 3, 4, 7]]) for sys_state in sys_states])
    
    return num_1478

def solve_part_two(file='../solutions/inputs/8.in'):
    sys_states = load_file(file)

    sum_outputs = 0

    for sys_state in sys_states:
        in_to_out = [0 for i in range(10)]
        in_to_out[1] = find_one(sys_state['wires'])
        in_to_out[4] = find_four(sys_state['wires'])
        in_to_out[7] = find_seven(sys_state['wires'])
        in_to_out[8] = find_eight(sys_state['wires'])
        find_six_seg_displays(in_to_out, sys_state['wires'])
        find_five_seg_displays(in_to_out, sys_state['wires'])

        sum_outputs += map_to_output(in_to_out, sys_state['outputs'])
        

    return sum_outputs

def find_one(wires):
    one_wire = next(w for w in wires if len(w) == 2)
    return ''.join(sorted(one_wire))

def find_four(wires):
    four_wire = next(w for w in wires if len(w) == 4)
    return ''.join(sorted(four_wire))

def find_seven(wires):
    seven_wire = next(w for w in wires if len(w) == 3)
    return ''.join(sorted(seven_wire))

def find_eight(wires):
    eight_wire = next(w for w in wires if len(w) == 7)
    return ''.join(sorted(eight_wire))

def find_six_seg_displays(in_to_out, wires):
    six_seg_wires = list(set([''.join(sorted(w)) for w in wires if len(w) == 6]))
    in_to_out[9] = next(w for w in six_seg_wires if len(filter(lambda c :c in in_to_out[4], w)) == 4)
    in_to_out[0] = next(w for w in six_seg_wires if len(filter(lambda c :c in in_to_out[1], w)) == 2 and w not in in_to_out)
    in_to_out[6] = next(w for w in six_seg_wires if w not in in_to_out)  

def find_five_seg_displays(in_to_out, wires):
    five_seg_wires = list(set([''.join(sorted(w)) for w in wires if len(w) == 5]))
    in_to_out[3] = next(w for w in five_seg_wires if len(filter(lambda c :c in in_to_out[1], w)) == 2)
    in_to_out[5] = next(w for w in five_seg_wires if len(filter(lambda c :c in in_to_out[6], w)) == 5)
    in_to_out[2] = next(w for w in five_seg_wires if w not in in_to_out)

def map_to_output(in_to_out, outputs):
    output_str = ''
    for o in outputs:
        val = in_to_out.index(''.join(sorted(o)))
        output_str += str(val)
    return int(output_str)

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    sys_states = [{'wires': l.split("|")[0].split(), 'outputs': l.split("|")[1].split()} for l in input.readlines()]
    return sys_states
