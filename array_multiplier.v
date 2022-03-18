`include "fa.v"

module array_mutliplier(a, b, a_t, b_t, p, p_t);
  input [3:0] a;
  input [3:0] b;
  input [3:0] a_t;
  input [3:0] b_t;
  output [7:0] p;
  output [7:0] p_t;
  
  wire w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28, w29, w30, w31;
  wire x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31;
  
  
  
  glfit_and g0 (a[3], b[0], a_t[3], b_t[0], w0, x0);
  glfit_and g1 (a[2], b[0], a_t[2], b_t[0], w1, x1);
  glfit_and g2 (a[1], b[0], a_t[1], b_t[0], w2, x2);
  glfit_and g3 (a[0], b[0], a_t[0], b_t[0], p[0], p_t[0]);
  glfit_and g4 (a[3], b[1], a_t[3], b_t[1], w3, x3);
  glfit_and g5 (a[2], b[1], a_t[2], b_t[1], w4, x4);
  glfit_and g6 (a[1], b[1], a_t[1], b_t[1], w5, x5);
  glfit_and g7 (a[0], b[1], a_t[0], b_t[1], w6, x6);
  glfit_and g8 (a[3], b[2], a_t[3], b_t[2], w7, x7);
  glfit_and g9 (a[2], b[2], a_t[2], b_t[2], w8, x8);
  glfit_and g10 (a[1], b[2], a_t[1], b_t[2], w9, x9);
  glfit_and g11 (a[0], b[2], a_t[0], b_t[2], w10, x10);
  glfit_and g12 (a[3], b[3], a_t[3], b_t[3], w11, x11);
  glfit_and g13 (a[2], b[3], a_t[2], b_t[3], w12, x12);
  glfit_and g14 (a[1], b[3], a_t[1], b_t[3], w13, x13);
  glfit_and g15 (a[0], b[3], a_t[0], b_t[3], w14, x14);

  fa f0 (w6, w2, 1'b0, x6, x2, 1'b0, p[1], w15, p_t[1], x15);
  fa f1 (w5, w1, 1'b0, x5, x1, 1'b0, w16, w17, x16, x17);
  fa f2 (w4, w0, 1'b0, x4, x0, 1'b0, w18, w19, x18, x19);
  fa f3 (w15, w10, w16, x15, x10, x16, p[2], w20, p_t[2], x20);
  fa f4 (w9, w17, w18, x9, x17, x18, w21, w22, x21, x22);
  fa f5 (w8, w3, w19, x8, x3, x19, w23, w24, x23, x2);
  fa f6 (w14, w20, w21, x14, x20, x21, p[3], w25, p_t[3], x25);
  fa f7 (w13, w22, w23, x13, x22, x23, w26, w27, x26, x27);
  fa f8 (w12, w7, w24, x12, x7, x24, w28, w29, x28, x29);
  fa f9 (w25, w26, 1'b0, x25, x26, 1'b0, p[4], w30, p_t[4], x30);
  fa f10 (w27, w30, w28, x27, x30, x28, p[5], w31, p_t[5], x31);
  fa f11 (w11, w31, w29, x11, x31, x29, p[6], p[7], p_t[6], p_t[7]);
  
endmodule
