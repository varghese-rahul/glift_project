import pyrtl 
from pyrtl.rtllib import libutils

from gates import *
from full_adder import *

def multiplier(a, b, a_t, b_t):

    p, p_t = [0]*8, [0]*8

    w0, x0 = and_gate(a[3], b[0], a_t[3], b_t[0])
    w1, x1 = and_gate(a[2], b[0], a_t[2], b_t[0])
    w2, x2 = and_gate(a[1], b[0], a_t[1], b_t[0])

    p[0], p_t[0] = and_gate(a[0], b[0], a_t[0], b_t[0])

    w3, x3 = and_gate(a[3], b[1], a_t[3], b_t[1])
    w4, x4 = and_gate(a[2], b[1], a_t[2], b_t[1])
    w5, x5 = and_gate(a[1], b[1], a_t[1], b_t[1])
    w6, x6 = and_gate(a[0], b[1], a_t[0], b_t[1])
    w7, x7 = and_gate(a[3], b[2], a_t[3], b_t[2])
    w8, x8 = and_gate(a[2], b[2], a_t[2], b_t[2])
    w9, x9 = and_gate(a[1], b[2], a_t[1], b_t[2])
    w10, x10 = and_gate(a[0], b[2], a_t[0], b_t[2])
    w11, x11 = and_gate(a[3], b[3], a_t[3], b_t[3])
    w12, x12 = and_gate(a[2], b[3], a_t[2], b_t[3])
    w13, x13 = and_gate(a[1], b[3], a_t[1], b_t[3])
    w14, x14 = and_gate(a[0], b[3], a_t[0], b_t[3])

    p[1], w15, p_t[1], x15 = full_adder(w6, w2, pyrtl.Const(0,1), x6, x2, pyrtl.Const(0,1))
    w16, w17, x16, x17 = full_adder(w5, w1, pyrtl.Const(0,1), x5, x1, pyrtl.Const(0,1))
    w18, w19, x18, x19 = full_adder(w4, w0, pyrtl.Const(0,1), x4, x0, pyrtl.Const(0,1))
    p[2], w20, p_t[2], x20 = full_adder(w15, w10, w16, x15, x10, x16)
    w21, w22, x21, x22 = full_adder(w9, w17, w18, x9, x17, x18)
    w23, w24, x23, x24 = full_adder(w8, w3, w19, x8, x3, x19)
    p[3], w25, p_t[3], x25 = full_adder(w14, w20, w21, x14, x20, x21)
    w26, w27, x26, x27 = full_adder(w13, w22, w23, x13, x22, x23)
    w28, w29, x28, x29 = full_adder(w12, w7, w24, x12, x7, x24)
    p[4], w30, p_t[4], x30 = full_adder(w25, w26, pyrtl.Const(0,1), x25, x26, pyrtl.Const(0,1))
    p[5], w31, p_t[5], x31 = full_adder(w27, w30, w28, x27, x30, x28)
    p[6], p[7], p_t[6], p_t[7] = full_adder(w11, w31, w29, x11, x31, x29)

    return pyrtl.concat_list(p), pyrtl.concat_list(p_t)

    

def multiplier_32bit(a_32, b_32, a_t_32, b_t_32, start, shifts=4):
    a_32, b_32, a_t_32, b_t_32 = pyrtl.match_bitwidth(a_32, b_32, a_t_32, b_t_32)

    alen = len(a_32)
    blen = len(b_32)
    a_tlen = len(a_t_32)
    b_tlen = len(b_t_32)
    areg = pyrtl.Register(alen)
    breg = pyrtl.Register(blen + alen)
    accum = pyrtl.Register(blen + alen)
    a_treg = pyrtl.Register(a_tlen)
    b_treg = pyrtl.Register(b_tlen + a_tlen)
    accum_t = pyrtl.Register(b_tlen + a_tlen)
    done = (areg == 0) 

    if (shifts > alen) or (shifts > blen) or (shifts > a_tlen) or (shifts > b_tlen):
        raise pyrtl.PyrtlError("shift is larger than one or both of the parameters A or B,"
                               "please choose smaller shift")


    with pyrtl.conditional_assignment:

        with start: 
            areg.next |= a_32
            breg.next |= b_32
            accum.next |= 0
            a_treg.next |= a_t_32
            b_treg.next |= b_t_32
            accum_t.next |= 0

        with ~done:  
            areg.next |= libutils._shifted_reg_next(areg, 'r', shifts)  
            breg.next |= libutils._shifted_reg_next(breg, 'l', shifts)  
            a_treg.next |= libutils._shifted_reg_next(a_treg, 'r', shifts) 
            b_treg.next |= libutils._shifted_reg_next(b_treg, 'l', shifts)  
            p, p_t = multiplier(areg, breg, a_treg, b_treg)
            accum.next |= accum + p
            accum_t.next |= accum_t + p_t

    return accum, accum_t, done