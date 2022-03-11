import pyrtl

from gates import *
BITMAX = 32

def half_adder(a, b, a_t, b_t):
    sum, sum_t = xor_gate(a, b, a_t, b_t)
    carry, carry_t = and_gate(a, b, a_t, b_t)
    return sum, carry, sum_t, carry_t

def full_adder(a, b, c, a_t, b_t, c_t):
    sum1, carry1, sum1_t, carry1_t = half_adder(a, b, a_t, b_t)
    sum2, carry2, sum2_t, carry2_t = half_adder(c, sum1, c_t, sum1_t)
    sum, sum_t = sum2, sum2_t
    carry, carry_t = or_gate(carry1, carry2, carry1_t, carry2_t)
    return sum, carry, sum_t, carry_t

def full_adder_32bit(a_32, b_32, c_32, a_t_32, b_t_32, c_t_32):
    s_32, s_t_32 = 0, 0 
    
    c, c_t = c_32 & 1, c_t_32 & 1 
    for i in range(BITMAX):
        a, b = a_32>>i & 1, b_32>>i & 1 
        a_t, b_t = a_t_32>>i & 1, b_t_32>>i & 1
        s, c, s_t, c_t = full_adder(a, b, c, a_t, b_t, c_t)
        s_32 += s<<i
        s_t_32 += s_t<<i
    return s_32, c, s_t_32, c_t