import pyrtl

from gates import *
from full_adder import *
from multiplier import *
from comparator import *


def execute(op, a, b, c=None, a_t=None, b_t=None, c_t=None):
    if op=="AND":
        o, o_t = and_gate(a, b, a_t, b_t)
    elif op=="OR":
        o, o_t = or_gate(a, b, a_t, b_t)
    elif op=="XOR":
        o, o_t = xor_gate(a, b, a_t, b_t)
    elif op=="XNOR":
        o, o_t = xnor_gate(a, b, a_t, b_t)
    elif op=="ADD":
        sum, carry, sum_t, carry_t = full_adder_32bit(a, b, c, a_t, b_t, c_t)
        o, o_t = [sum, carry], [sum_t, carry_t]
    elif op=="MULT":
        o, o_t = multiplier_32bit(a, b, a_t, b_t)
    elif op=="COMP":
        less, equal, greater, less_t, equal_t, greater_t = comparator_32bit(a, b, a_t, b_t)
        o, o_t = [less, equal, greater], [less_t, equal_t, greater_t]

    return o, o_t



    
if __name__=='__main__':
    a = input("enter a: ")
    b = input("enter b: ")
    c = input("enter c: ")
    a_t = input("enter a_t: ")
    b_t = input("enter b_t: ")
    c_t = input("enter c_t: ")
    # o,o_t= full_adder_32bit(int(a),int(b),int(c), int(a_t),int(b_t), int(c_t))
    o,o_t= execute("ADD", int(a),int(b),int(c), int(a_t),int(b_t), int(c_t))
    print(o,o_t)
