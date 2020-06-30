# Joshua Chan
# 1588459
def selection_sort_descend_trace(number):

    for i in range(len(number) - 1):
        largest = i
        for j in range(i + 1, len(number)):
            if number[j] > number[largest]:
                largest = j
        number[i], number[largest] = number[largest], number[i]
        print(' '.join([str(x) for x in number]))
    return number
    # The function will continue to move the largest number behind the last largest number until it is completely sorted

if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
