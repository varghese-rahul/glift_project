import pyrtl

from gates import *


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

