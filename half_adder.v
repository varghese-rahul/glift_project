`include "glfit_and.v"
`include "glfit_or.v"
`include "glfit_xor.v"
`include "glfit_xnor.v"


module half_adder (input a, input b,input a_t, input b_t, output sum, output carry, output sum_t, output carry_t);
  
  glfit_xor g1(a, b, a_t, b_t, sum, sum_t);
  glfit_and g2(a, b, a_t, b_t, carry, carry_t);
 
endmodule
