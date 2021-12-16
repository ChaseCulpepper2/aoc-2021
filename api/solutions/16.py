# https://adventofcode.com/2021/day/14
# https://adventofcode.com/2021/day/14#part2

import os, sys
from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)

hex_to_bin = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",    
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "A":"1010",
   "B":"1011",
   "C":"1100",
   "D":"1101",
   "E":"1110",
   "F":"1111",
}

def solve_part_one(file):
    hex = load_file(file)
    bits = ''.join([hex_to_bin[h] for h in hex])
    print(bits)
    versions = 0
    i = 1

    while len(bits) > 8:
        print(' '.join(['Processing packet', str(i), 'of length', str(len(bits))]))
        val, version, packet_length = process_packet(bits)
        versions += version
        bits = bits[packet_length:]
        i += 1
        
    return versions

def solve_part_two(file):
    hex = load_file(file)
    bits = ''.join([hex_to_bin[h] for h in hex])
    print(bits)
    versions = 0
    i = 1

    while len(bits) > 8:
        print(' '.join(['Processing packet', str(i), 'of length', str(len(bits))]))
        val, version, packet_length = process_packet(bits)
        versions += version
        bits = bits[packet_length:]
        i += 1

    return val

def process_packet(bits, tabs = '\t'):
    if len(bits) <= 8: return 0, 0
    version = int(bits[0:3], 2)
    print(tabs + 'Version: ' + bits[0:3])
    type_id = int(bits[3:6], 2)
    print(tabs +'type_id: ' + bits[3:6])
    packet_length = 0
    if type_id == 4:
        val, literal_length = parse_literal_packet(bits, tabs)
        packet_length += literal_length + 6
    else:
        val, sum_versions, operation_length = parse_operation_packet(bits, tabs)
        version += sum_versions
        packet_length += operation_length + 6

    return val, version, packet_length

def parse_literal_packet(bits, tabs):
    i = 0
    literal = ''
    while bits[6+i*5] == '1':
        literal += bits[7+i*5:11+i*5]
        i += 1
    
    literal += bits[7+i*5:11+i*5]
    print(tabs + 'literal bits:' + literal)
    val = int(literal, 2)
    print(tabs + 'val: ' + str(val))

    return val, len(literal)+i+1

def parse_operation_packet(bits, tabs):
    length_type_id = bits[6]
    operation_length = 1
    sum_versions = 0
    vals = []
    print(tabs + 'Length_Type_id: ' + str(length_type_id))

    if length_type_id == '0':
        operation_length += 15
        subpacket_length = int(bits[7:22], 2)
        #operation_length += subpacket_length
        processed_subpacket_length = 0
        print(tabs + 'subpackets length: ' + bits[7:22])
        subpacket_i = 1

        while processed_subpacket_length < subpacket_length:
            if len(bits[6+operation_length + processed_subpacket_length:]) <= 8: break
            val, version, subpacket_length_i = process_packet(bits[6+operation_length + processed_subpacket_length:], tabs+'\t')
            vals.append(val)
            sum_versions += version
            processed_subpacket_length += subpacket_length_i
            subpacket_i += 1
    else:
        operation_length += 11
        num_subpackets = int(bits[7:18], 2)
        processed_subpacket_length = 0
        print(tabs+'subpackets count: ' + bits[7:18])

        for subpacket_i in range(num_subpackets):
            if len(bits[6+operation_length + processed_subpacket_length:]) <= 8: break
            val, version, subpacket_length_i = process_packet(bits[6+operation_length + processed_subpacket_length:], tabs+'\t')
            vals.append(val)
            sum_versions += version
            processed_subpacket_length += subpacket_length_i

    out_val = perform__operation(int(bits[3:6], 2), vals)

    operation_length += processed_subpacket_length

    return out_val, sum_versions, operation_length

def perform__operation(type_id, vals):
    ret = -1
    if type_id == 0:
        ret = sum(vals)
    elif type_id == 1:
        ret = 1
        for v in vals:
            ret *= v
    elif type_id == 2:
        ret = min(vals)
    elif type_id == 3:
        ret = max(vals)
    elif type_id == 5:
        ret = 1 if vals[0] > vals[1] else 0
    elif type_id == 6:
        ret = 1 if vals[0] < vals[1] else 0
    elif type_id == 7:
        ret = 1 if vals[0] == vals[1] else 0          
        
    return ret



def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    return input.read()
