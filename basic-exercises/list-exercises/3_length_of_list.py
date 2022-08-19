# -*- coding: utf-8 -*-
"""
Find length of list

"""

def lenght_find(my_list):
    
    count = 0
    
    for element in my_list:
        count += 1
    
    return count

test_list = [12, 35, 9, 56, 24]

lengt = lenght_find(test_list)

print(lengt)