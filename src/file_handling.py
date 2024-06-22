# Open a file in write mode
file = open('newFile.txt', 'w')
file.write("This a new file!\n")
file.close()

# Open a file in read mode
file = open('newFile.txt', 'r')
content = file.read()
print(content)
file.close()

# Open a file in append mode
file = open('newFile.txt', 'a')
file.write("This is my second line!\n")
file.close()

# with statement
with open ('newFile.txt', 'r') as file:
	content = file.read()
	print(content)