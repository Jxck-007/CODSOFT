from pathlib import Path
class Todolist():
    def __init__(self):
        self.tasks=[]
        if Path('To-Do.txt').exists():
            with open("To-Do.txt","r") as file:
                A=file.readlines()
                self.tasks=[B.strip() for B in A]
            print("Tasks are load from file")
        else:
            print("File not found ,starting a new file to save data")
            with open ('To-Do.txt','a+')as file:
                file.write("")
    def ADD(self,Add):
        self.tasks.append(Add)
    def VIEW(self):
        for i,task in enumerate(self.tasks,start=1):
            print(i,'-',task)
    def REMOVE(self):
        try:
            x=int(input('Enter the task number to remove:'))
            x-=1
            self.tasks.pop(x)
            print('task has been removed successfully')
            print()
        except:
            print("Error,Task Not Found")
            print()
    def SAVE(self):
        with open("To-Do.txt","w") as file:
                for _ in self.tasks:
                    file.write(_+'\n')         
    def EXIT(self):
        pass
a=Todolist()
while(True):          
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")
    option=int(input("Enter a your option:"))
    if (option==1):
        Add=input("Enter the task:")
        a.ADD(Add)
        a.SAVE()
        print("Task Added Successfully")
        print()
    elif(option==2):
        print("your Remaining Task(s) are:")
        a.VIEW()
        print()
    elif(option==3):
        a.REMOVE()
        a.SAVE()
    elif(option==4):
        a.EXIT
        a.SAVE()
        break
    else:
        print("Invalid Choice")
        print()
