import pyrtl

from gates import *
from gates_32bit import *
from full_adder import *
from multiplier import *
from comparator import *


def execute(op, a, b, a_t, b_t, c=None, c_t=None):
    if op=="AND":
        o, o_t = and_gate_32bit(a, b, a_t, b_t)
    elif op=="OR":
        o, o_t = or_gate_32bit(a, b, a_t, b_t)
    elif op=="XOR":
        o, o_t = xor_gate_32bit(a, b, a_t, b_t)
    elif op=="XNOR":
        o, o_t = xnor_gate_32bit(a, b, a_t, b_t)
    elif op=="ADD":
        sum, carry, sum_t, carry_t = full_adder_32bit(a, b, c, a_t, b_t, c_t)
    elif op=="MULT":
        p, p_t = multiplier_32bit(a, b, a_t, b_t)
    elif op=="COMP":
        less, equal, greater, less_t, equal_t, greater_t = comparator_32bit(a, b, a_t, b_t)



