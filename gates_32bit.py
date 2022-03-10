import pyrtl

from gates import *

def and_gate_32bit(a_32, b_32, a_t_32, b_t_32):
    assert (len(a_32) == len(b_32) == len(a_t_32) == len(b_t_32) == 32)

    o_32, o_t_32 = '', ''
    for i in range(31,-1,-1):
        o, o_t = and_gate(a_32[i], b_32[i], a_t_32[i], b_t_32[i])
        o_32.append(o)
        o_t_32.append(o_t)

    return o_32, o_t_32

def or_gate_32bit(a_32, b_32, a_t_32, b_t_32):
    assert (len(a_32) == len(b_32) == len(a_t_32) == len(b_t_32) == 32)

    o_32, o_t_32 = '', ''
    for i in range(31,-1,-1):
        o, o_t = or_gate(a_32[i], b_32[i], a_t_32[i], b_t_32[i])
        o_32.append(o)
        o_t_32.append(o_t)

    return o_32, o_t_32

def xor_gate_32bit(a_32, b_32, a_t_32, b_t_32):
    assert (len(a_32) == len(b_32) == len(a_t_32) == len(b_t_32) == 32)

    o_32, o_t_32 = '', ''
    for i in range(31,-1,-1):
        o, o_t = xor_gate(a_32[i], b_32[i], a_t_32[i], b_t_32[i])
        o_32.append(o)
        o_t_32.append(o_t)

    return o_32, o_t_32


def xnor_gate_32bit(a_32, b_32, a_t_32, b_t_32):
    assert (len(a_32) == len(b_32) == len(a_t_32) == len(b_t_32) == 32)

    o_32, o_t_32 = '', ''
    for i in range(31,-1,-1):
        o, o_t = xnor_gate(a_32[i], b_32[i], a_t_32[i], b_t_32[i])
        o_32.append(o)
        o_t_32.append(o_t)

    return o_32, o_t_32