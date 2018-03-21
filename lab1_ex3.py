print("Insert a task")
task=input()
print("Insert another task")
task1=input()
print("Insert another task")
task2=input()
print("Enter a task you want to be deleted")
delete=input()
print("Lists of tasks:")
if(task == delete):
    task = None
    print(task1 + " " + task2)
elif (task1 == delete):
    task1 = None
    print(task + " " + task2)
elif(task2 == delete):
    task2 = None
    print(task + " " + task1)
