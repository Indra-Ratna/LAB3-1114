"""
Indra Ratna
CS - UY 1114
21 Sept 2018
Lab 3
"""

import random
x = random.randint(97,122)
y = random.randint(97,122)
z = random.randint(97,122)

print (str(chr(x))+str(chr(y))+str(chr(z)))
print( str(chr(x))+str(chr(z))+str(chr(y))+" "+str(((x+y+z)>(x+z+y))))
print(str(chr(y))+str(chr(x))+str(chr(z))+" "+str(((x+y+z)>(y+x+z))))
print(str(chr(y))+str(chr(z))+str(chr(x))+" "+str(((x+y+z)>(y+z+x))))
print(str(chr(z))+str(chr(x))+str(chr(y))+" "+str(((x+y+z)>(z+x+y))))
print(str(chr(z))+str(chr(y))+str(chr(x))+" "+str(((x+y+z)>(z+y+x))))
