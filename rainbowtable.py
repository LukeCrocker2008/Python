import sys
import hashlib

dictionary = sys.argv[1]
rainbowtxt = sys.argv[2]

rainbowtable = {}   # Dictionary to hold rainbow table

with open(dictionary) as file:
    for password in file:
        password.strip(' ')
        password = password.replace("\n", "")
        hash = hashlib.new('md4')
        hash.update(password.encode("utf_16_le"))
        rainbowtable[hash.hexdigest()] = password

file.close()

for entry in sorted(rainbowtable):
    print(entry, ":", rainbowtable[entry])
