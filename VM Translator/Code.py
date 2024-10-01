class CodeWriter:

    def push_pop_writer(self,command, arg1, arg2,file_name):
        name_of_file = self.remove_file_extension(file_name)
        address = self.get_assembly_address(arg1)
        return_str = ""
        if command == "C_PUSH":
            return_str = self.push_assembly(address,arg1,arg2,name_of_file)
        elif command == "C_POP":
            return_str = self.pop_assembly(address, arg1, arg2, name_of_file)

        return return_str


    def arithemetic_writer(self,command,line_number):
        return_string = f"//added assembly code that does {command}\n"
        if "add" in command:
           return_string += self.add_assembly()
        elif "sub" in command:
           return_string += self.sub_assembly()
        elif "eq" in command:
            return_string += self.eq_assembly(line_number)
        elif "gt" in command:
            return_string += self.gt_assembly(line_number)
        elif "lt" in command:
            return_string += self.lt_assembly(line_number)
        elif "and" in command:
             return_string += self.and_assembly()
        elif "or" in command:
             return_string += self.or_assembly()
        elif "not" in command:
             return_string += self.not_assembly()
        elif "neg" in command:
             return_string += self.neg_assembly()

        return return_string


    @staticmethod
    def get_assembly_address(arg1):
        return_str = ""
        if "local" in arg1:
            return_str = 'LCL'
        elif  "argument" in arg1:
            return_str = "ARG"
        elif "constant" in arg1:
            return_str = "CONS"
        elif "this" in arg1:
            return_str = "THIS"
        elif "that" in arg1:
            return_str = "THAT"
        elif "temp" in arg1:
            return_str = "TEMP"
        return return_str

    @staticmethod
    def remove_file_extension(file_name):
        dot_index = file_name.find(".")
        return file_name[:dot_index]


    @staticmethod
    def push_assembly(address, arg1, arg2, name_of_file):
        assembly_str = f"// added assembly code that does [push {arg1} {arg2.strip()}]\n"

        if arg1.strip() in ["local", "argument", "this", "that"]:
            # segment (local, argument, this, that)
            assembly_str += (f"@{address}\n"  # Load base address (e.g., LCL, ARG)
                             f"D=M\n"  # D = base address
                             f"@{arg2.strip()}\n"  # Load index
                             f"A=D+A\n"  # A = base + index
                             f"D=M\n"  # D = *A (value to push)
                             f"@SP\n"
                             f"A=M\n"  # Point to top of stack
                             f"M=D\n"  # Push value onto stack
                             f"@SP\n"
                             f"M=M+1\n")  # SP++ (increment stack pointer)

        elif "constant" in arg1:
            # Push constant value
            assembly_str += (f"@{arg2.strip()}\n"  # Load constant value
                             f"D=A\n"  # D = constant value
                             f"@SP\n"
                             f"A=M\n"  # Point to top of stack
                             f"M=D\n"  # Push constant onto stack
                             f"@SP\n"
                             f"M=M+1\n")  # SP++

        elif "static" in arg1:
            # Push static segment value
            assembly_str += (f"@{name_of_file.strip()}.{arg2.strip()}\n"
                             f"D=M\n"  # D = static value
                             f"@SP\n"
                             f"A=M\n"  # Point to top of stack
                             f"M=D\n"  # Push static value onto stack
                             f"@SP\n"
                             f"M=M+1\n")  # SP++

        elif "temp" in arg1:
            # Push temp segment value (R5 + index)
            assembly_str += (f"@{5 + int(arg2.strip())}\n"  # R5 + index
                             f"D=M\n"  # D = temp value
                             f"@SP\n"
                             f"A=M\n"  # Point to top of stack
                             f"M=D\n"  # Push temp value onto stack
                             f"@SP\n"
                             f"M=M+1\n")  # SP++

        elif "pointer" in arg1:
            # Push pointer segment (THIS/THAT)
            pointer_segment = "THIS" if int(arg2) == 0 else "THAT"
            assembly_str += (f"@{pointer_segment}\n"
                             f"D=M\n"  # D = pointer value
                             f"@SP\n"
                             f"A=M\n"  # Point to top of stack
                             f"M=D\n"  # Push pointer value onto stack
                             f"@SP\n"
                             f"M=M+1\n")  # SP++

        return assembly_str

    @staticmethod
    def pop_assembly(address, arg1, arg2, name_of_file):
        assembly_str = f"// added assembly code that does [pop {arg1} {arg2.strip()}]\n"

        if arg1.strip() in ["local", "argument", "this", "that"]:
            # segment (local, argument, this, that)
            assembly_str += (f"@{address}\n"
                             f"D=M\n"  # D = base address (e.g., LCL, ARG)
                             f"@{arg2.strip()}\n"
                             f"D=D+A\n"  # D = base + i
                             f"@R13\n"
                             f"M=D\n"  # Store target address in R13
                             f"@SP\n"
                             f"AM=M-1\n"  # SP-- and point to top of stack
                             f"D=M\n"  # D = *SP (value to pop)
                             f"@R13\n"
                             f"A=M\n"
                             f"M=D\n")  # Store popped value into target address

        elif "static" in arg1:
            # Static segment
            assembly_str += (f"@SP\n"
                             f"AM=M-1\n"  # SP-- and point to top of stack
                             f"D=M\n"  # D = *SP (value to pop)
                             f"@{name_of_file.strip()}.{arg2.strip()}\n"
                             f"M=D\n")  # Store value in static variable

        elif "temp" in arg1:
            # Temp segment (R5 + index)
            assembly_str += (f"@SP\n"
                             f"AM=M-1\n"  # SP-- and point to top of stack
                             f"D=M\n"  # D = *SP (value to pop)
                             f"@{5 + int(arg2.strip())}\n"  # R5 + index
                             f"M=D\n")  # Store value in temp segment

        elif "pointer" in arg1:
            # Pointer segment (THIS/THAT)
            pointer_segment = "THIS" if int(arg2) == 0 else "THAT"
            assembly_str += (f"@SP\n"
                             f"AM=M-1\n"  # SP-- and point to top of stack
                             f"D=M\n"  # D = *SP (value to pop)
                             f"@{pointer_segment}\n"
                             f"M=D\n")  # Store value in THIS or THAT

        return assembly_str


    @staticmethod
    def add_assembly():
        return (f"@SP\n"  # Load address of stack pointer
                f"AM=M-1\n"  # Decrement SP and point to top of stack
                f"D=M\n"  # D = first operand (top of stack)
                f"A=A-1\n"  # Move A to the second operand (new top of stack)
                f"M=D+M\n"  # Add the two values and store the result
               )

    @staticmethod
    def sub_assembly():
        return (f"@SP\n"  # Load address of stack pointer
                f"AM=M-1\n"  # Decrement SP and point to top of stack
                f"D=M\n"  # D = first operand (top of stack)
                f"A=A-1\n"  # Move A to the second operand (new top of stack)
                f"M=M-D\n"  # Subtract the two values and store the result
                )

    @staticmethod
    def eq_assembly(line_number):
        return (f"@SP\n"  # Load address of stack pointer
                f"AM=M-1\n"  # Decrement SP and point to the top of the stack
                f"D=M\n"  # D = first operand (top of stack)
                f"A=A-1\n"  # Decrement SP again to get the second operand
                f"D=M-D\n"  # D = second operand - first operand
                f"@EQ_TRUE_LABEL{line_number}\nD;JEQ\n"  # If D == 0 (first == second), jump to TRUE_LABEL
                f"@SP\nA=M-1\nM=0\n"  # Otherwise, set the result to 0 (false)
                f"@EQ_CONTINUE_LABEL{line_number}\n0;JMP\n"  # Jump to continue
                f"(EQ_TRUE_LABEL{line_number})\n"  # TRUE_LABEL: for the case where first == second
                f"@SP\nA=M-1\nM=-1\n"  # Set the result to -1 (true)
                f"(EQ_CONTINUE_LABEL{line_number})\n"  # CONTINUE_LABEL: to continue after comparison
                )

    @staticmethod
    def gt_assembly(line_number):
        return (f"@SP\n"  # Load address of stack pointer
                f"AM=M-1\n"  # Decrement SP and point to the top of the stack
                f"D=M\n"  # D = first operand (top of stack)
                f"A=A-1\n"  # Decrement SP again to get the second operand
                f"D=M-D\n"  # D = second operand - first operand
                f"@EQ_TRUE_LABEL{line_number}\nD;JGT\n"  # If D == 0 (first == second), jump to TRUE_LABEL
                f"@SP\nA=M-1\nM=0\n"  # Otherwise, set the result to 0 (false)
                f"@EQ_CONTINUE_LABEL{line_number}\n0;JMP\n"  # Jump to continue
                f"(EQ_TRUE_LABEL{line_number})\n"  # TRUE_LABEL: for the case where first == second
                f"@SP\nA=M-1\nM=-1\n"  # Set the result to -1 (true)
                f"(EQ_CONTINUE_LABEL{line_number})\n"  # CONTINUE_LABEL: to continue after comparison
                )

    @staticmethod
    def lt_assembly(line_number):
        return (f"@SP\n"  # Load address of stack pointer
                f"AM=M-1\n"  # Decrement SP and point to the top of the stack
                f"D=M\n"  # D = first operand (top of stack)
                f"A=A-1\n"  # Decrement SP again to get the second operand
                f"D=M-D\n"  # D = second operand - first operand
                f"@EQ_TRUE_LABEL{line_number}\nD;JLT\n"  # If D == 0 (first == second), jump to TRUE_LABEL
                f"@SP\nA=M-1\nM=0\n"  # Otherwise, set the result to 0 (false)
                f"@EQ_CONTINUE_LABEL{line_number}\n0;JMP\n"  # Jump to continue
                f"(EQ_TRUE_LABEL{line_number})\n"  # TRUE_LABEL: for the case where first == second
                f"@SP\nA=M-1\nM=-1\n"  # Set the result to -1 (true)
                f"(EQ_CONTINUE_LABEL{line_number})\n"  # CONTINUE_LABEL: to continue after comparison
                )

    @staticmethod
    def and_assembly():
        return(f"@SP\nAM=M-1\nD=M\n"
               f"A=A-1\nM=D&M\n"
               )

    @staticmethod
    def or_assembly():
        return(f"@SP\nAM=M-1\nD=M\n"
               f"A=A-1\nM=D|M\n"
              )

    @staticmethod
    def not_assembly():
        return f"@SP\nA=M-1\nM=!M\n"

    @staticmethod
    def neg_assembly():
        return f"@SP\nA=M-1\nM=-M\n"

    @staticmethod
    def stop_code():
        return  f"(STOP)\n@STOP\n0;JMP"


