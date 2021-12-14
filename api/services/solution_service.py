import os, sys
import imp

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+'/solutions')

def get_solution(day, test=False):
    imp.find_module(str(day))
    mod = __import__(str(day))
    file = get_solution_input_file(day, test)

    part_one_func = getattr(mod, "solve_part_one")
    part_two_func = getattr(mod, "solve_part_two")

    return {'part_one': part_one_func(file), 'part_two': part_two_func(file)}
    
def get_solution_input_file(day, test):
    file = '../solutions/inputs/' + str(day) + ('.test' if test else '.in')
    return file