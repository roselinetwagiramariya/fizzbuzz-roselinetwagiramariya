# add your code here
start = int(input("What is the starting value?"))
stop = int(input("Where to stop"))
step = int(input("How far should we step?"))

for i in range(start,stop,step):
    if i % 5 == 0 and i % 10 == 0:
        print("ROSEMOO")
    elif i % 2 == 0:
        print("ROSE")
    elif i % 5 == 0:
        print("MOO")
    else:
        print(i)
    
