from Parser import Parser

class SymbolTable:
    symbol_table = {}
    variable_start = 16

    def __str__(self):
        return f'{self.symbol_table} is the state of the symbol table'

    def __init__(self,file_name):
        self.init_symbol_table()
        self.add_label_symbols(file_name)

    def init_symbol_table(self):
        self.symbol_table = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,

        }

    def add_entry(self,var_name):
        self.symbol_table[var_name]=self.variable_start
        self.variable_start += 1

    def contains(self, var_name):
        if var_name in self.symbol_table:
            return True
        else:
            return False

    def get_address(self,var_name):
        return str(self.symbol_table[var_name])

    def add_label_symbols(self,file_name):
        parser = Parser()
        file = open(file_name, 'r')
        program_counter=0
        for line in file:
            if "//" in line or line == "\n":
                continue
            instruction_type = parser.instruction_type(line)
            if instruction_type == 'L_INSTRUCTION':
                label_str=self.get_label_string(line)
                self.symbol_table[label_str]=program_counter
                continue
            program_counter += 1
        file.close()

    @staticmethod
    def get_label_string(label_string: str):
        index_of_parenthesis = label_string.find(')')
        return label_string[1:index_of_parenthesis].strip()