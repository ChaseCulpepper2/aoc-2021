import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+'/solutions')

def get_solution(day):
    solutions = {}
    mod = __import__(str(day))
    func = getattr(mod, "solve_part_one")
    solutions['part_one'] = func()

    func = getattr(mod, "solve_part_two")
    solutions['part_two'] = func()

    return solutions