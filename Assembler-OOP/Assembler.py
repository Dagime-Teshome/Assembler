from Parser import Parser
from Code import Code
from SymbolTable import  SymbolTable


def get_comp_type_binary(comp_binary, destination_binary, jump_binary):
    c_prefix = "111"
    return c_prefix + comp_binary + destination_binary + jump_binary
def file_loop(file_name):
    symbol_table = SymbolTable(file_name)
    pars_file = open(file_name, 'r')
    binary = Code()
    parser = Parser()
    binary_string=""
    for line in pars_file:
        if "//" in line or line == "\n":
            continue
        match parser.instruction_type(line):
            case 'A_INSTRUCTION':
                binary_string+=binary.symbol(parser.symbol(line.strip(), symbol_table)) + "\n"
            case 'C_INSTRUCTION':
                comp_binary = binary.comp(parser.comp(line.strip()))
                dest_binary = binary.dest(parser.dest(line.strip()))
                jmp_binary = binary.jump(parser.jmp(line.strip()))
                binary_string += get_comp_type_binary(comp_binary, dest_binary, jmp_binary) + '\n'
    pars_file.close()
    return binary_string

def write_to_file(file_name,binary):
    index = file_name.find('.')
    new_file_name = file_name[0:index]
    file = open(new_file_name +".bin",'w')
    file.write(binary.strip())
    file.close()
    return new_file_name

def main():
    file_name = input("Please enter file name with extension: ")
    binary_content=file_loop(file_name)
    new_file = write_to_file(file_name,binary_content)
    print(f'Program finished.Binary code can be found in file {new_file}')


main()




