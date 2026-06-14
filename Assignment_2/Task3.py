


with open("myfile.txt", "w") as file:
    print("Enter text (type END to finish):")

    while True:
        line = input()

        if line == "END":
            break

        file.write(line + "\n")

print("Text written to file successfully!")
#python automatically closes file stream after exiting with block