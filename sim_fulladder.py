import pyrtl

from full_adder import *


a, b, c = pyrtl.Input(1, 'a'), pyrtl.Input(1, 'b'), pyrtl.Input(1, 'c')
a_t, b_t, c_t = pyrtl.Input(1, 'a_t'), pyrtl.Input(1, 'b_t'), pyrtl.Input(1, 'c_t') 

sum, carry, sum_t, carry_t = full_adder(a, b, c, a_t, b_t, c_t)


a_list = ['1','1','1']
b_list = [1,1,1]
c_list = [1,1,1]
a_t_list = [1,1,1]
b_t_list = [1,1,1]
c_t_list = [1,1,1]

# simulate the instantiated design for 15 cycles
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(3):
    sim.step({
        'a' : bool(a_list[cycle]),
        'b' : b_list[cycle],
        'c' : c_list[cycle],
        'a_t': a_t_list[cycle],
        'b_t': b_t_list[cycle],
        'c_t': c_t_list[cycle]
    })
    sum_val, sum_t_val = sim.inspect(sum), sim.inspect(sum_t)
    carry_val, carry_t_val = sim.inspect(carry), sim.inspect(carry_t)
    print(sum_val, carry_val, sum_t_val, carry_t_val)
    

sim_trace.render_trace()



# 'a' : random.choice([0, 1]),
# 'b' : random.choice([0, 1]),
# 'c' : random.choice([0, 1]),
# 'a_t': random.choice([0, 1]),
# 'b_t': random.choice([0, 1]),
# 'c_t': random.choice([0, 1])