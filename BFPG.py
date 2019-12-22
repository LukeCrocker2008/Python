# BFPG.py

import math
import time

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

passwordLength = int(input("Enter the password length: "))

iPossibilities = math.pow(float(len(chars)), float(passwordLength) )
print(str(iPossibilities) + " words total.")

start = time.time()
i = 0
while i < iPossibilities:
    theword = ''
    val = i
    j = 0
    while j < passwordLength:
        ch = val % len(chars)
        theword = chars[int(ch)] + theword
        val = val / len(chars)
        j += 1
    print(theword)
    i += 1
end = time.time()
difftime = (end - start) * 1000
print ("It took " + str(difftime) + " milliseconds to generate " + str(iPossibilities) + " possible combinations")
