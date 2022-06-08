f = open("dates12.py", "x")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("dates12.py", "r")
print(f.read())