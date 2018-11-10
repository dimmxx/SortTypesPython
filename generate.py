import random
import time

LIST_LEN = 1000

def data_Int(length, start, end):
    data_int = []
    for i in range (length):
        data_int.append((random.randint(start, end)))
    return data_int

def data_Float(length, start, end):
    data_float = []
    for i in range (length):
        data_float.append((round(random.uniform(start, end), 4)))
    return data_float

def data_51():
    data_51 = []
    for i in range (52):
        data_51.append(i)
    return data_51

f = open('data.py', 'w')
f.write('DATA_INT = ' + str(list(data_Int(LIST_LEN, 0, 1000))) + '\n' + 'DATA_FLOAT = '
                      + str(list(data_Float(LIST_LEN, 0.0, 1000.0))) +'\n' + 'data_51 = '
                      + str(data_51()))
f.close()

