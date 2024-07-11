def getDInsBinary(D_ins):
    D_bin="";
    #check destination codes
    if D_ins == "null":
        D_bin = "000";
    elif D_ins == "M":
        D_bin = "001";
    elif D_ins == "D":
        D_bin = "010";
    elif D_ins == "DM" or D_ins == "MD":
        D_bin = "011";
    elif D_ins == "A":
        D_bin = "100";
    elif D_ins == "AM":
        D_bin = "101";        
    elif D_ins == "AD":
        D_bin = "110";
    elif D_ins == "ADM":
        D_bin = "111"; 
    return D_bin.strip();
    
def getJInsBinary(J_ins):
    J_bin="";
    #check jump codes
    if J_ins == "null":
        J_bin = "000";
    elif J_ins == "JGT":
        J_bin = "001";
    elif J_ins == "JEQ":
        J_bin = "010";
    elif J_ins == "JGE":
        J_bin = "011";
    elif J_ins == "JLT":
        J_bin = "100";
    elif J_ins == "JNE":
        J_bin = "101";
    elif J_ins == "JLE":
        J_bin = "110";
    elif J_ins == "JMP":
        J_bin = "111";
    return J_bin.strip();


def getCInsBinary(C_ins):
    C_bin=""
    a="";
    #evaluate a code
    index = C_ins.find("M");
    if index != -1:
        a="1";
    else:
        a="0";
    #check cccc codes 
    if C_ins == "0":
        C_bin="101010";
    elif C_ins == "1":
        C_bin="111111";
    elif C_ins == "-1":
        C_bin="111010";        
    elif C_ins == "D":
        C_bin="001100";
    elif C_ins == "A" or C_ins == "M":
        C_bin="110000";
    elif C_ins == "!D":
        C_bin="001101";
    elif C_ins == "!A" or C_ins == "!M":
        C_bin="110001";
    elif C_ins == "-D":
        C_bin="001111";
    elif C_ins == "-A" or C_ins == "-M":
        C_bin="110011"        
    elif C_ins == "D+1":
        C_bin="011111";
    elif C_ins == "A+1" or C_ins == "M+1":
        C_bin="110111";
    elif C_ins == "D-1":
        C_bin="001110";         
    elif C_ins == "A-1" or C_ins == "M-1":
        C_bin="110010";
    elif C_ins == "D+A" or C_ins == "D+M":
        C_bin="000010";
    elif C_ins == "D-A" or C_ins == "D-M":
        C_bin="010011";    
    elif C_ins == "A-D" or C_ins == "M-D":
        C_bin="000111";
    elif C_ins == "D&A" or C_ins == "D&M":
        C_bin="000000";
    elif C_ins == "D|A" or C_ins == "D|M":
        C_bin="010101";
    # concatent and return
    binary = a + C_bin;
    return binary.strip();
         
def comp(instruction):
    semi_index=instruction.find(';');
    equals_index=instruction.find('=');
    
    if semi_index != -1 and equals_index != -1:
        comp_instruction=instruction[equals_index:semi_index];
    elif semi_index == -1:
        comp_instruction = instruction[equals_index+1:];
    elif equals_index == -1:
        comp_instruction = instruction[0:semi_index];
    #else:
       # print("error");
        #return
    return comp_instruction.strip();
    
def dest(instruction):
    index = instruction.find('=');
    if index == -1:
        return "null"
    else:
        dest_instruction = instruction[0:index];
        return dest_instruction.strip();
    
    
def jmp(instruction):
    #find index of semicolon
    index = instruction.find(';');
    if index == -1:
        return "null"
    else:
        jmp_instruction = instruction[index+1:]
        return jmp_instruction.strip();
    
def label(instruction):
    index = instruction.find(')');
   
    return instruction[1:index].strip();
    
def symbol(a_ins,symbolTable,var_start):
    
    sym_var= a_ins.strip();
    var_str = sym_var[1:];
    ret_ins= "";
    if(var_str.isdecimal()):
        ret_ins = var_str;
    else:
        
        if var_str in symbolTable:
            ret_ins = str(symbolTable[var_str]);
        else:
            symbolTable[var_str]=var_start[0];
            var_start[0]+=1;
            ret_ins = str(symbolTable[var_str]);
    
    return ret_ins;

def typeOfInstruction(instruction):
    instructionType="";
    if "@" in instruction:
        instructionType='A_INSTRUCTION';
    elif "=" in instruction or ";" in instruction:
        instructionType='C_INSTRUCTION';
    elif "(" in instruction or ")" in instruction:
        instructionType='L_INSTRUCTION';
    return instructionType;

def getCTypeBinary(C_ins,D_ins,J_ins):
    c_prefix="111"
    C_bin = getCInsBinary(C_ins);
    D_bin = getDInsBinary(D_ins);
    J_bin = getJInsBinary(J_ins);
    return c_prefix+C_bin+D_bin+J_bin;

def gerSTypeBinary(A_ins):
    
    A_Bin="0"+"{0:b}".format(int(A_ins));
    full_A_Bin=A_Bin.zfill(16);
    return full_A_Bin;


    

def parseFile(fileName,symbol_Table,var_start):
    
    file=open(fileName,'r');
    binContent="";
    for line in file:
        
        if "//" in line or line == "\n" :
            continue;
        
        instructiontype=typeOfInstruction(line);
        
        if instructiontype == "A_INSTRUCTION":
            
            binary=gerSTypeBinary(symbol(line,symbol_Table,var_start));
            binContent += binary + '\n';
            
        elif instructiontype == "C_INSTRUCTION":
            binary = getCTypeBinary(comp(line),dest(line),jmp(line));
            binContent += binary + '\n';
            
        #elif instructiontype == "L_INSTRUCTION":
            #label_str = label(line);
            #binary = getLBinary(label_str,symbol_Table);
            #pass
    file.close();
    writeToFile(fileName,binContent);
    
def writeToFile(fileName,binContent):
    index = fileName.find('.');
    newFileName = fileName[0:index];
    file = open(newFileName +".bin",'w');
    file.write(binContent.strip());
    file.close;


def intSymbolTable():
    return {
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
     
    
def intialParse(fileName,symbolTable):
    
    file=open(fileName,'r');
    pc = 0;
    label_str ="";
    for line in file:
        if "//" in line or line == "\n" :
            continue;
        
        instructiontype=typeOfInstruction(line);
        
        if instructiontype == "L_INSTRUCTION":
            label_str = label(line);
            symbolTable[label_str] = pc;
            continue;
        pc += 1;
    file.close();
    
def main():
    var_start=[16];
    symbol_Table = intSymbolTable();
    fileName=input("Please enter file name with extension: ");
    intialParse(fileName,symbol_Table);
    parseFile(fileName,symbol_Table,var_start);
     
   
main();
    