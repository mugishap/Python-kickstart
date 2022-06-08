number = int(input("Enter number of names: "))
names = []

for i in range (number):
    name = input("Enter your name please: ")
    names.append(name)

for i in range(number):
    print(names[i])