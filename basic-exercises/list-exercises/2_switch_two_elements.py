# -*- coding: utf-8 -*-

"""
Python program to swap two elements in a list

Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
Examples: 
 

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

"""



def switch_two_elements(my_list, index_one, index_two):
        
    if not len(my_list):
        return print("The list is empty!")
    
    new_list = my_list.copy()
    
    new_list[index_one] = my_list[index_one]
    new_list[index_two] = my_list[index_two]
    
    return new_list


test_list = [12, 35, 9, 56, 24]

switched_list =  switch_two_elements(test_list, 2, 4)

print(switched_list)