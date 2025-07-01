def ADD(Add):
    with open ('To-Do.txt','a+') as A:        
        A.write(Add +'\n') 
def VIEW():
    with open('To-Do.txt','r') as V:
        x=V.readlines()
        for _,i in enumerate(x,start=1):
            print(_,'- ',i,end='')
            print()
def REMOVE():
    try:
        with open('To-Do.txt','r') as R:
            a=R.readlines() 
        with open('To-Do.txt','w') as R:
            x=int(input("Enter the number of the task to remove:")) 
            for i,line in enumerate(a,start=1):   
                if(i!=x):
                    R.write(line)        
    except:
        print("Error,Task Not Found")  
while(True):          
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")
    option=int(input("Enter a your option:"))
    if (option==1):
        Add=input("Enter the task:")
        ADD(Add)
        print("Task Added Successfully")
        print()
    elif(option==2):
        print("Your Remaining Task(s) are:")
        VIEW()
    elif(option==3):
        REMOVE()
        print()
    elif(option==4):
        break
    else:
        print("Invalid Choice")