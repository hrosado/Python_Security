"""Python Functions and managing exceptions."""

# Example syntax in book doesnt provide a good example
# sequence = [100,200,300,400]
def contains(sequence, item):
    for element in sequence:
        if element == item:
            return True
    return False

print( contains([100,200,300,400], 200))

# Managing exceptions
# Divide by zero exception
# try:
#     print("[+] 10/0 =" + str(10/0))
# except ValueError:
#     print("Error = " + str(ValueError))

# File not found exception
# try:
#     #f = file("file.txt") # depricated
#     f = open("file.txt")
# except ValueError:
#     print("File not found = " + str(ValueError))

