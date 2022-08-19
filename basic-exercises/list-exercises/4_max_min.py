# -*- coding: utf-8 -*-
"""
Maximum and minimum of two numbers in Python
"""

def maximum(num_1, num_2):
    
    if num_1 >= num_2:
        return num_1
    
    elif num_2 > num_1:
        return num_2
    
    
def minimum(num_1, num_2):
    
    if num_1 <= num_2:
        return num_1
    
    elif num_2 < num_1:
        return num_2
    
test_num_1, test_num_2 = 3, 5

maximum_num = maximum(test_num_1, test_num_2)

minimum_num = minimum(test_num_1, test_num_2)

print("Max number:", maximum_num, "Min number:" , minimum_num)