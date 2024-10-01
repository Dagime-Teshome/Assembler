// added assembly code that does [push  constant 17]
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 17]
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL3
D;JEQ
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL3
0;JMP
(EQ_TRUE_LABEL3)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL3)
// added assembly code that does [push  constant 17]
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 16]
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL6
D;JEQ
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL6
0;JMP
(EQ_TRUE_LABEL6)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL6)
// added assembly code that does [push  constant 16]
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 17]
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL9
D;JEQ
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL9
0;JMP
(EQ_TRUE_LABEL9)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL9)
// added assembly code that does [push  constant 892]
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 891]
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL12
D;JLT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL12
0;JMP
(EQ_TRUE_LABEL12)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL12)
// added assembly code that does [push  constant 891]
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 892]
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL15
D;JLT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL15
0;JMP
(EQ_TRUE_LABEL15)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL15)
// added assembly code that does [push  constant 891]
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 891]
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL18
D;JLT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL18
0;JMP
(EQ_TRUE_LABEL18)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL18)
// added assembly code that does [push  constant 32767]
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 32766]
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL21
D;JGT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL21
0;JMP
(EQ_TRUE_LABEL21)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL21)
// added assembly code that does [push  constant 32766]
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 32767]
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL24
D;JGT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL24
0;JMP
(EQ_TRUE_LABEL24)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL24)
// added assembly code that does [push  constant 32766]
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 32766]
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
@EQ_TRUE_LABEL27
D;JGT
@SP
A=M-1
M=0
@EQ_CONTINUE_LABEL27
0;JMP
(EQ_TRUE_LABEL27)
@SP
A=M-1
M=-1
(EQ_CONTINUE_LABEL27)
// added assembly code that does [push  constant 57]
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 31]
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  constant 53]
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// added assembly code that does [push  constant 112]
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
//added assembly code that does neg
@SP
A=M-1
M=-M
//added assembly code that does and
@SP
AM=M-1
D=M
A=A-1
M=D&M
// added assembly code that does [push  constant 82]
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//added assembly code that does or
@SP
AM=M-1
D=M
A=A-1
M=D|M
//added assembly code that does not
@SP
A=M-1
M=!M
(STOP)
@STOP
0;JMP