class Parser:

    @staticmethod
    def instruction_type(line):
        inst_type = ""
        if "@" in line:
            inst_type = 'A_INSTRUCTION'
        elif "=" in line or ";" in line:
            inst_type = 'C_INSTRUCTION'
        elif "(" in line or ")" in line:
            inst_type = 'L_INSTRUCTION'
        return inst_type

    @staticmethod
    def symbol(line, symbol_table):
        symbol_str = line[1:]
        if symbol_str.isdecimal():
            return symbol_str
        else:
            if not symbol_table.contains(symbol_str) :
                symbol_table.add_entry(symbol_str)
            return  symbol_table.get_address(symbol_str)



    @staticmethod
    def dest(line):
        index = line.find('=')

        if index == -1:
            dest_instruction = "null"
        else:
            dest_instruction = line[0:index]

        return dest_instruction.strip()

    @staticmethod
    def jmp(line):
        # find index of semicolon
        index = line.find(';')

        if index == -1:
            jmp_instruction = "null"
        else:
            jmp_instruction = line[index + 1:]

        return jmp_instruction.strip()


    @staticmethod
    def comp(line):
        semi_index = line.find(';')
        equals_index = line.find('=')

        if semi_index != -1 and equals_index != -1:
            comp_instruction = line[equals_index:semi_index]
        elif semi_index == -1:
            comp_instruction = line[equals_index + 1:]
        elif equals_index == -1:
            comp_instruction = line[0:semi_index]

        return comp_instruction.strip()