`include "glfit_and.v"
`include "glfit_or.v"
`include "glfit_xor.v"
`include "glfit_xnor.v"

module comparator (input [3:0] a, input [3:0] b,input [3:0] a_t, input [3:0] b_t, output less, output equal, output greater, output less_t, output equal_t, output greater_t);

  wire a3 = a[3];
  wire a2 = a[2];
  wire a1 = a[1];
  wire a0 = a[0];
  wire b3 = b[3];
  wire b2 = b[2];
  wire b1 = b[1];
  wire b0 = b[0];
  
  wire a3_t = a_t[3];
  wire a2_t = a_t[2];
  wire a1_t = a_t[1];
  wire a0_t = a_t[0];
  wire b3_t = b_t[3];
  wire b2_t = b_t[2];
  wire b1_t = b_t[1];
  wire b0_t = b_t[0];
  
  wire a3n_t, b3n_t, a3n, b3n;
  wire a2n_t, b2n_t, a2n, b2n;
  wire a1n_t, b1n_t, a1n, b1n;
  wire a0n_t, b0n_t, a0n, b0n;
  
  not not1 (a3n, a3);
  not not2 (b3n, b3);
  not not3 (a2n, a2);
  not not4 (b2n, b2);
  not not5 (a1n, a1);
  not not6 (b1n, b1);
  not not7 (a0n, a0);
  not not8 (b0n, b0);
  
  
  not not9 (a3n_t, a3_t);
  not not10 (b3n_t, b3_t);
  not not11 (a2n_t, a2_t);
  not not12 (b2n_t, b2_t);
  not not13 (a1n_t, a1_t);
  not not14 (b1n_t, b1_t);
  not not15 (a0n_t, a0_t);
  not not16 (b0n_t, b0_t);
  
  wire n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 ,n11, n12;
  wire n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24;
  wire n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36;
  
  wire p1, p2, p3, p4, p5, p6, p7, p8, p9, p10;
  wire q1, q2, q3, q4, q5, q6, q7, q8, q9, q10;
  
  // EQUAL TO
  
  glfit_xnor g8(a3, b3, a3_t, b3_t, n13, n14);
  glfit_xnor g9(a2, b2, a2_t, b2_t, n15, n16);
  glfit_xnor g10(a1, b1, a1_t, b1_t, n17, n18);
  glfit_xnor g11(a0, b0, a0_t, b0_t, n19, n20);
  
  glfit_and g12(n13, n15, n14, n16, n21, n22);
  glfit_and g13(n17, n21, n18, n22, n23, n24);
  glfit_and g14(n19, n23, n20, n24, equal, equal_t);
  
 //	GREATER THAN
  
  glfit_and g1(a3, b3n, a3_t, b3n_t, n1, n2);

  
  glfit_and g2(a2, b2n, a2_t, b2n_t, n3, n4);
  glfit_and h1(n13, n3, n14, n4, p1, p2);
  
  
  glfit_and g3(a1, b1n, a1_t, b1n_t, n5, n6);
  glfit_and h2(n13, n15 , n14, n16, p3, p4);
  glfit_and h3(p3, n5, p4, n6, p5, p6);
  
  glfit_and g4(a0, b0n, a0_t, b0n_t, n7, n8);
  //glift_and h2(n13, n15 , n14, n16, p3, p4);
  glfit_and h4(p3, n17, p4, n18, p7, p8);
  glfit_and h5(p7, n7, p8, n8, p9, p10);
 
  glfit_or g5(n1, p1, n2, p2, n9, n10);
  glfit_or g6(p5, n9, p6, n10, n11, n12);
  glfit_or g7(p9, n11, p10, n12, greater, greater_t);
  
  // LESS THAN
  
  glfit_and g15(a3n, b3, a3n_t, b3_t, n25, n26);
  
  glfit_and g16(a2n, b2, a2n_t, b2_t, n27, n28);
  glfit_and h6(n13, n27, n14, n28, q1, q2);
  
  glfit_and g17(a1n, b1, a1n_t, b1_t, n29, n30);
  glfit_and h7(n13, n15 , n14, n16, q3, q4); //repetition
  glfit_and h8(q3, n29, q4, n30, q5, q6);
  
  glfit_and g18(a0n, b0, a0n_t, b0_t, n31, n32);
  //glift_and h7(n13, n15 , n14, n16, q3, q4);
  glfit_and h9(q3, n17, q4, n18, q7, q8); //repetition
  glfit_and h10(q7, n31, q8, n32, q9, q10);
  
  glfit_or g19(n25, q1, n26, q2, n33, n34);
  glfit_or g20(q5, n33, q6, n34, n35, n36);
  glfit_or g21(q9, n35, q10, n36, less, less_t);
 
endmodule

module tb;
  
  reg [3:0] a;
  reg [3:0] b;
  reg [3:0] a_t;
  reg [3:0] b_t;
  wire less, equal, greater, less_t, equal_t, greater_t;
  //wire o_t;
  


  //glfit_and dut(a, b, a_t, b_t, o_t);
  //glfit_or dut(a, b, a_t, b_t, o_t);
  //glfit_xor dut(a, b, a_t, b_t, o_t);
  comparator dut(a, b, a_t, b_t, less, equal, greater, less_t, equal_t, greater_t); 

  initial begin

    $monitor(less, equal, greater, less_t, equal_t, greater_t); 

    #5
    a = 4'b1111;
    b = 4'b1111;
    a_t = 4'b1111;
    b_t = 4'b1111;
    
    #5
    a = 4'b0111;
    b = 4'b1111;
    a_t = 4'b1111;
    b_t = 4'b1111;

    #5
    a = 4'b1111;
    b = 4'b0111;
    a_t = 4'b1111;
    b_t = 4'b1111;
    
    #10
    
    $finish;
 
  end
  
  initial begin
      $dumpfile("dump.vcd");
      $dumpvars(0,tb);
  end
  
endmodule
