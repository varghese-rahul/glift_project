`include "half_adder.v"

module fa(input a, input b, input c, input a_t, input b_t, input c_t, output sum, output carry, output sum_t, output carry_t);

	wire sum1;
  	wire sum2;
  	wire carry1;
  	wire carry2;
  	wire sum1_t;
  	wire sum2_t;
  	wire carry1_t;
  	wire carry2_t;
  
    
  half_adder ha1(a, b, a_t, b_t, sum1, carry1, sum1_t, carry1_t);
  half_adder ha2(c, sum1, c_t, sum1_t, sum2, carry2, sum2_t, carry2_t);


  assign sum = sum2;  
  
  assign sum_t = sum2_t;  
 
  glfit_or g1(carry1, carry2, carry1_t, carry2_t, carry, carry_t);
    
endmodule
