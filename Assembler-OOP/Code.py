class Code:

    @staticmethod
    def dest(destination_instruction):
        destination_binary = ""
        # check destination codes
        if (destination_instruction
                == "null"):
            destination_binary = "000"
        elif (destination_instruction
              == "M"):
            destination_binary = "001"
        elif (destination_instruction
              == "D"):
            destination_binary = "010"
        elif (destination_instruction
              == "DM" or destination_instruction
              == "MD"):
            destination_binary = "011"
        elif (destination_instruction
              == "A"):
            destination_binary = "100"
        elif (destination_instruction
              == "AM"):
            destination_binary = "101"
        elif (destination_instruction
              == "AD"):
            destination_binary = "110"
        elif (destination_instruction
              == "ADM"):
            destination_binary = "111"
        return destination_binary.strip()

    @staticmethod
    def comp(comp_instruction):
        computation_binary = ""
        a = ""
        # evaluate a code
        index = comp_instruction.find("M")
        if index != -1:
            a = "1"
        else:
            a = "0"
        # check cccc codes
        if comp_instruction == "0":
            computation_binary = "101010"
        elif comp_instruction == "1":
            computation_binary = "111111"
        elif comp_instruction == "-1":
            computation_binary = "111010"
        elif comp_instruction == "D":
            computation_binary = "001100"
        elif comp_instruction == "A" or comp_instruction == "M":
            computation_binary = "110000"
        elif comp_instruction == "!D":
            computation_binary = "001101"
        elif comp_instruction == "!A" or comp_instruction == "!M":
            computation_binary = "110001"
        elif comp_instruction == "-D":
            computation_binary = "001111"
        elif comp_instruction == "-A" or comp_instruction == "-M":
            computation_binary = "110011"
        elif comp_instruction == "D+1":
            computation_binary = "011111"
        elif comp_instruction == "A+1" or comp_instruction == "M+1":
            computation_binary = "110111"
        elif comp_instruction == "D-1":
            computation_binary = "001110"
        elif comp_instruction == "A-1" or comp_instruction == "M-1":
            computation_binary = "110010"
        elif comp_instruction == "D+A" or comp_instruction == "D+M":
            computation_binary = "000010"
        elif comp_instruction == "D-A" or comp_instruction == "D-M":
            computation_binary = "010011"
        elif comp_instruction == "A-D" or comp_instruction == "M-D":
            computation_binary = "000111"
        elif comp_instruction == "D&A" or comp_instruction == "D&M":
            computation_binary = "000000"
        elif comp_instruction == "D|A" or comp_instruction == "D|M":
            computation_binary = "010101"
        # concatent and return
        binary = a + computation_binary
        return binary.strip()

    @staticmethod
    def jump(jump_instruction):
        jump_binary = ""
        # check jump codes
        if jump_instruction == "null":
            jump_binary = "000"
        elif jump_instruction == "JGT":
            jump_binary = "001"
        elif jump_instruction == "JEQ":
            jump_binary = "010"
        elif jump_instruction == "JGE":
            jump_binary = "011"
        elif jump_instruction == "JLT":
            jump_binary = "100"
        elif jump_instruction == "JNE":
            jump_binary = "101"
        elif jump_instruction == "JLE":
            jump_binary = "110"
        elif jump_instruction == "JMP":
            jump_binary = "111"
        return jump_binary.strip()

    @staticmethod
    def symbol(a_ins):
        a_binary = "0" + "{0:b}".format(int(a_ins))
        full_a_binary = a_binary.zfill(16)
        return full_a_binary