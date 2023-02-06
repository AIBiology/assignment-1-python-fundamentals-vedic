#!/usr/bin/env python

import find_max


def test_max():
    '''Test the find_max function in find_max.py'''
    tests= []
    tests.append([3,45,78,2,53,1,0])
    tests.append([-2,-6,-23,-646])
    tests.append([0.5,-1.4,5.3,-2.44])

    for test in tests:
        assert find_max.find_max(test) == max(test), f'Hmm...your find_max function failed my test: {find_max.find_max(test)} is not the maximum value in {test}.'

test_max

