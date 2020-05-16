import math

pi = 3.14
i = 0

fname = input("Input filename:")

try :
    fhandler = open(fname, 'w')
except :
    print("Something wrong.")
    quit()

while i < 2 * pi + 0.01:
    tmp = math.sin(i)
    fhandler.write(str(tmp) + "\n")
    i = i + 0.01
