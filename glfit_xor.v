module glfit_xor (input a, input b, input a_t, input b_t, output o, output o_t);
  
  wire an_t, bn_t, an, bn;
  
  wire i1, i6, i7;
  
  
  not not1 (an_t, a_t);
  
  not not2 (bn_t, b_t);
    
  
  and and1 (i1, a_t, b_t);
  
  
  // XOR GATE 
  
  and and6 (i6, an_t, b_t);
  
  and and7 (i7, a_t, bn_t);
  
  or or3 (o_t, i1, i6, i7);
  
  //REGULAR XOR
  
  xor xor1 (o, a, b);
  
  
endmodule
