data = [7, 3, 2, 99, 4, 9, 9, 1, 1]
print(data)

def swap(index1, index2, data):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp


def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i, len(data), 1):
            if data[j] < data[min_index]:
                min_index = j

        swap(min_index, i, data)

selection_sort(data)
print(data)


