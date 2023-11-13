"""Dictionaries allow us to associate values with keys.
The KEY is IMMUTABLE, but the value can be changed.
Dictionaries are associative matrices."""


# Dictionaries
services = {"FTP":21,"HTTP":80,"SMTP":25,"SSH":22}
services2 = {"FTP":21,"HTTP":80,"SNMP":161,"LDAP":389}

services.update(services2)

print(services)
# services["FTP"] =8080
print(services.keys())
print(services.values())
print(services.items())

items = services.items()
print(items)

print(type(services))
print(type(items))
print(services.items())


keys = services.keys()
print(keys)
# Depracated -> services.has_key('http')

for key,value in services.items():
    print(key,value)


