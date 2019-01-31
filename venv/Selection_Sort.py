#Petar Crljenica
#I will be doing the selection sort algorithm here. I will be referencing the algroithm from GeeksforGeeks
#to do this. I will try to use the description to make the code myself without referencing the code already there.

import sys
import array
import random
from timeit import default_timer as timer

class selection_sort:
    def __init__(self):
        self.myarray = []
        self.total_cells_in_array = random.randint(1, 10000)
        self.min_element = 1
        self.max_element = 10000

    def gen_rand(self):

        for i in range(self.total_cells_in_array):
            self.myarray.append(random.randint(self.min_element, self.max_element))

    def print_array(self):
        for i in range(len(self.myarray)):
            print(self.myarray[i], end=' ')
        print('\n')

    def the_sorting(self):
        arr_length = len(self.myarray)
        i = 0
        for i in range(arr_length-1):
            min_index = i
            j = i + 1
            for j in range(j, arr_length):
                if(self.myarray[j] < self.myarray[min_index]):
                    min_index = j
            self.myarray[i], self.myarray[min_index] = self.myarray[min_index], self.myarray[i]

        return self.print_array()

if __name__ == '__main__':
    my_sort = selection_sort()
    my_sort.gen_rand()
    my_sort.print_array()
    start = timer()
    my_sort.the_sorting()
    end = timer()
    print("The time it took to sort this array of length", my_sort.total_cells_in_array, "was", end-start)