def list_task():
    print("list tasks");
    line_count = 0;
    f = open("todo.txt",'a+');
    f.seek(0)
     
    for line in f:
        print("* "+"(" + str(line_count) +")" + line.strip());
        line_count += 1;
    f.close();
    
def add_task(task):
    print("add "+ task + "to list");
    fileObject = open("todo.txt","a+");
    fileObject.write(task + "\n");
    fileObject.close();
    
def remove_task(task_no):
    f=open("todo.txt",'r+');
    line_count = 0;
    content = ""
    for line in f:
        if line_count != task_no:    
            content += line;
        line_count += 1;
    f.close();
    f=open("todo.txt","w");
    f.write(content);
    f.close;
def main():
    
    
    command = " ";
    while command != "Exit":
        command = input("Do you want to List , Add , Remove or Exit? ");
        if command == "List":
            list_task();
            
        elif command == "Add":
            task = input("What task should be added? ");
            add_task(task);
        elif command == "Remove":
            task_no = int(input("what task should be removed? "));
            remove_task(task_no);
    print("Program Terminated");
    
main();