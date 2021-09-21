number = [1,2,3]
name = ["Prabhat","Rahul","Prithvi"]

zipped = zip(number,name)

for i in zipped:
    print(i)

for no,n in zip(number,name):
    print(no,n)