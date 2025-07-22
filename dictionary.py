#
d={}
loop=True
while loop==True:

    name = input("Enter your name")
    marks = float(input("Enter your marks"))
    d[name]=marks
    ans=input("Do you wish to continue? y/n").lower()
    if ans=='y' or ans=='yes':
        loop=True
    else:
        loop=False

#print(d)
for key,value in d.items():
    print(key,value)
