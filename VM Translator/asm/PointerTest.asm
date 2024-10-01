// added assembly code that does [push  constant 3030]
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [pop  pointer 0]
@SP
AM=M-1
D=M
@THIS
M=D
// added assembly code that does [push  constant 3040]
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [pop  pointer 1]
@SP
AM=M-1
D=M
@THAT
M=D
// added assembly code that does [push  constant 32]
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [pop  this 2]
@THIS
D=M
@2
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// added assembly code that does [push  constant 46]
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [pop  that 6]
@THAT
D=M
@6
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// added assembly code that does [push  pointer 0]
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// added assembly code that does [push  pointer 1]
@THAT
D=M
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
// added assembly code that does [push  this 2]
@THIS
D=M
@2
A=D+A
D=M
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
// added assembly code that does [push  that 6]
@THAT
D=M
@6
A=D+A
D=M
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
(STOP)
@STOP
0;JMP