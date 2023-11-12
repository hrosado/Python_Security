"""Comprehension Lists
Comprehension lists allow you to create a new list of iterable objects."""

# Example syntax
# new_list = [expression for_loop_one_or_more condition]

# List comprehensions can also be used toiterate over strings:
protocolList = ["FTP","HTTP","SNMP","SSH"]

protocolList_Lower = [protocol.lower() for protocol in protocolList]
print(protocolList_Lower)

protocolList_Lower_Mod = [protocol.lower() for protocol in protocolList if "TP" in protocol]
print(protocolList_Lower_Mod)

print(protocolList[0])