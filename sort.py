import time
import inspect
from data import *


def gen_newlist(param):
    if param == 1:
       data = list(DATA_INT)
    elif param == 2:
        data = list(DATA_FLOAT)
    return data


def print_data(method_name, data_length, time_spent, data):
    if len(data) > 50:
        print('[', end='')
        for i in range(7):
            print(data[i], '', sep=', ', end='')
        print(data[7], ' ..... ', sep='', end='')
        for i in range(len(data) - 7, len(data) - 1, 1):
            print(data[i], '', sep=', ', end='')
        print(data[len(data) - 1], ']', sep='', end='\n')
    else:
        print(data)
    print('Sort type: ' + method_name)
    print('List length: ' + data_length)
    print('Time spent: ' + time_spent)
    print('----------------------------------------------------------------------------------------------------------')
    return 0


def insert_pos(index, dest, data):
         temp = data[index]
         for i in range(index, dest, -1):
             data[i] = data[i - 1]
         data[dest] = temp


def swap(index1, index2, data):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp


# ------------------------------------------------------------------------------------------------------------------


def gnome_sort_stupid_sort(data):
     print(data)
     start = time.time()
     i = 0
     while i != len(data) - 1:
         if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data [i + 1] = temp
                i = 0
                continue
         i += 1
     end = time.time()
     print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)
     return 0


def bubble_sort(data):
     print(data)
     start = time.time()
     trigger = True
     while trigger == True:
         trigger = False
         for i in range(len(data) - 1):
              if data[i] > data[i + 1]:
                   temp = data[i]
                   data[i] = data[i + 1]
                   data [i + 1] = temp
                   trigger = True
     end = time.time()
     print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)
     return 0


def bubble_sort_m(data):
     print(data)
     start = time.time()
     trigger = True
     k = 0
     while trigger == True:
         trigger = False
         for i in range((len(data) - 1) - k):
              if data[i] > data[i + 1]:
                   temp = data[i]
                   data[i] = data[i + 1]
                   data [i + 1] = temp
                   trigger = True
         k += 1
     end = time.time()
     print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)
     return 0


def shaker_sort(data):
     print(data)
     start = time.time()
     trigger = True
     run = 0
     while trigger:
         trigger = False
         for i in range(run, len(data) - 1 - run, 1):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
         run += 1
         for i in range(len(data) - 1 - run, run - 1, -1):
            if data[i] < data[i - 1]:
                temp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = temp
                trigger = True
     end = time.time()
     print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)
     return 0


def insertion_sort(data):
    print(data)
    start = time.time()
    for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                if data[i + 1] <= data[0]:
                    insert_pos(i + 1, 0, data)
                elif data[i + 1] > data[0]:
                    for j in range(i + 1):
                        if data[i + 1] <= data[j]:
                            insert_pos(i + 1, j, data)
    end = time.time()
    print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)
    return 0


def selection_sort(data):
    print(data)
    start = time.time()
    for i in range(len(data)):
        min_index = i
        for j in range(i, len(data), 1):
            if data[j] < data[min_index]:
                min_index = j

        swap(min_index, i, data)
    end = time.time()
    print_data(inspect.stack()[0][3], str(len(data)), str(end - start), data)


#gnome_sort_stupid_sort(gen_newlist(1))
bubble_sort(gen_newlist(1))
bubble_sort_m(gen_newlist(1))
shaker_sort(gen_newlist(1))
insertion_sort(gen_newlist(1))
selection_sort(gen_newlist(1))


