#selection sort
import time
import random
from typing import List

import random      
def select_sort (array):    
    for i in range(len(array)):   
        for j in range(i,len(array)):  
            if array[i] > array[j]:  
                tmp = array[i]
                array[i] = array[j]
                array [j] = tmp
if __name__ == "__main__":
    array = []     
    for i in range(50):    
        array.append(random.randrange(1000))
    print(array)
    select_sort(array)  
    print(array)
