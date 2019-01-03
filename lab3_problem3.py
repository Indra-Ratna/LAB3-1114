"""
Indra Ratna
CS-UY 1114
Lab 3
"""
import math

x = 0.0
y = (1/math.sqrt(2*math.pi))*(math.exp(-0.5*(x*x)))
print ("The value of the pdf at x = "+str(x)+" is "+ str(y))
x = 1.0
y = (1/math.sqrt(2*math.pi))*(math.exp(-0.5*(x*x)))
print ("The value of the pdf at x = "+str(x)+" is "+ str(y))
x = -1.0
y = (1/math.sqrt(2*math.pi))*(math.exp(-0.5*(x*x)))
print ("The value of the pdf at x = "+str(x)+" is "+ str(y))
