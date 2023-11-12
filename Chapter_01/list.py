protocolList = []

protocolList.append("ftp")

protocolList.append("ssh")

protocolList.append("smtp")

protocolList.append("http")

print(protocolList)

protocolList.sort() # Alphabetical order
print(protocolList)

print(type(protocolList))
print(len(protocolList))

# To access specific positions we use the index method.
position = protocolList.index("ssh")
print(f"ssh position {position}")
print(position)

# To remove a specific position we use the remove method.
protocolList.remove("ssh")
print(protocolList)

count = len(protocolList)
print(f"Protocol elements {count}")

# To print out the whole protocolList via loop
for protocol in protocolList:
    print(protocol)

# Lists also have methods
# .append(value): appends an element to the end of the list
# .count('x'): Gets the number of 'x' in the list.
# .index('x'): Returns the index of 'x' in the list.
# .insert('y','x'): Inserts the 'x' at the location of 'y'.
# .pop(): Returns the last elements and also removes it from the list.
# .remove('x'): Removes the first 'x' from the list.
# .reverse()
# .sort(): Sorts the list ...

# protocolList.reverse()
protocolList[::1]
print(protocolList)




