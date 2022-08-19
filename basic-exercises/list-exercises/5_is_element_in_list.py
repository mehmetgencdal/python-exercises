# -*- coding: utf-8 -*-
"""
Is element exist in the list?
"""

def is_in_list(my_list, element):
    
    if element in my_list:
        return True

    else:
        return False


test_list = [12, 35, 9, 56, 24]

element = 35
    
result = is_in_list(test_list, element)

print(result)