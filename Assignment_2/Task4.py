with open("myfile.txt", "r") as file:
    content = file.read()

print(content)

#python automatically closes file stream after exiting with block