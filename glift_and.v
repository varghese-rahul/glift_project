// Code your design here

module glfit_and (input a, input b, input a_t, input b_t, output o, output o_t);
  
  wire an_t, bn_t, an, bn;
  
  wire i1, i2, i3;
  
  
  not not1 (an_t, a_t);
  
  not not2 (bn_t, b_t);
  
  
  and and1 (i1, a_t, b_t);
  
  
  // AND GATE (CARRY FOR HALF ADDER / ONE BIT MULTIPLIER)
  
  and and2 (i2, a, an_t, b_t);
  
  and and3 (i3, b, a_t, bn_t);
  
  or or1 (o_t, i1, i2, i3);
  
  //REGULAR AND
  
  and and4 (o, a, b);

endmodule
