import numpy as np
import sys

data = sys.argv[1];
code = "";
counter = 1

for i in range(len(data)):
    if i == len(data)-1:
        if data[i] == data[i-1]:
            code += str(counter) + str(int(data[i]))
            print(code)
        else:
            code += str(int(1)) + str(int(data[i]))
            print(code)
    elif data[i+1]==data[i]:
        counter+=1
    else:
        code += str(counter) + str(int(data[i]))
        counter = 1
