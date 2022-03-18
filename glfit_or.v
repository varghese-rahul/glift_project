module glfit_or (input a, input b, input a_t, input b_t, output o, output o_t);
  
  wire an_t, bn_t, an, bn;
  
  wire i1, i4, i5;
  
  
  not not1 (an_t, a_t);
  
  not not2 (bn_t, b_t);
  
  not not3 (an, a);
  
  not not4 (bn, b);
  
  
  and and1 (i1, a_t, b_t);
  
  
  // OR GATE
  
  and and4 (i4, an, an_t, b_t);
  
  and and5 (i5, bn, a_t, bn_t);
  
  or or2 (o_t, i1, i4, i5);
  
  //REGULAR OR
  
  or or3 (o, a, b);
  
endmodule
