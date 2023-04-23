#!/usr/bin/env python

def find_max(nums):
    '''Takes in a list of numbers and returns the highest number'''
    max = nums[0]
    #default max value is 0
    for i in range(0,len(nums),1):
        if max < nums[i]:
            max = nums[i]
            #iterate through entire list. If the number at a position 
            #is greater than the maximum, then it is the new maximum
    
    return max