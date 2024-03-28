# add your code here
start = int(input("What is the starting value?"))
stop = int(input("Where to stop"))
step = int(input("How far should we step?"))

for i in range(start,stop,step):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
________________________________________________________________
start = int(input("What is the starting value?"))
stop = int(input("Where to stop"))
step = int(input("How far should we step?"))

for i in range(start,stop,step):
    if i % 2 == 0 and i % 4 == 0:
        print("FIZZBUZZ")
    elif i % 2 == 0:
        print("FIZZ")
    elif i % 4 == 0:
        print("BUZZ")
    else:
        print(i)
________________________________________________________________
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
