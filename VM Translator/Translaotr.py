from Parser import Parser
from Code import CodeWriter

def file_loop(file_name):
    pars_file = open(r"./tests/"+file_name, 'r')
    parser= Parser()
    code = CodeWriter()
    assembly_code=""
    line_number = 0
    for line in pars_file:
        if '//' in line or line == "\n":
            continue
        # print(line,parser.command_type(line))
        line_number += 1
        if parser.command_type(line) != 'C_ARITHMETIC':
            assembly_code += code.push_pop_writer(parser.command_type(line),parser.arg1(line),parser.arg2(line),file_name)
        elif parser.command_type(line) == 'C_ARITHMETIC':
            assembly_code += code.arithemetic_writer(parser.arg1(line,parser.command_type(line)),line_number)

    assembly_code += code.stop_code()
    pars_file.close()
    return assembly_code

def write_to_file(file_name,binary):
    code = CodeWriter()
    new_file_name = code.remove_file_extension(file_name)
    file = open(r"./asm/"+new_file_name +".asm",'w')
    file.write(binary.strip())
    file.close()
    return new_file_name

def main():
    file_name = input("Please enter file name with extension:")
    assembly_content=file_loop(file_name)
    new_file = write_to_file(file_name,assembly_content)
    print(f'Program finished.assembly code can be found in file {new_file}.asm')


main()




