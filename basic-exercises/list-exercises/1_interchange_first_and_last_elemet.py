# -*- coding: utf-8 -*-
"""
Python program to interchange first and last elements in a list

Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""

def interchange_first_and_last_element(my_list):
        
    if not len(my_list):
        return print("The list is empty!")
    
    new_list = my_list.copy()
    
    new_list[-1] = my_list[0]
    new_list[0] = my_list[-1]

    return new_list


test_list = [12, 35, 9, 56, 24]

interchange_list =  interchange_first_and_last_element(test_list)

print(interchange_list)