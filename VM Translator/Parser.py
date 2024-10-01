class Parser:

    @staticmethod
    def command_type(line):
        c_type = ""
        if "push" in line:
            c_type = "C_PUSH"
        elif "pop" in line:
            c_type = "C_POP"
        elif "add" in line or "sub" in line or "neg" in line or "eq" in line or "gt" in line or "lt" in line or  "and" in line or "or" in line or "not" in line:
            c_type = "C_ARITHMETIC"

        return c_type

    @staticmethod
    def arg1 (line,commandtype =''):
        if commandtype == "C_ARITHMETIC":
            return line.strip()
        start = line.index(' ')
        end = line.rindex(' ')
        return line[start:end]

    @staticmethod
    def arg2 (line):
        end = line.rindex(' ')
        return line[end:]


