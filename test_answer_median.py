#!/usr/bin/env python

import statistics
import find_median

def test_median():
    '''Test the find_median function in find_median.py '''
    tests= []
    tests.append([3,45,78,2,53,1,0])
    tests.append([1,2,3,4,5,6,7,8,9,10])
    tests.append([1,2,3,4,5,5,7,8,9,10])
    tests.append([1,2,3,5,5,5,7,8,9,10])
    tests.append([-1,-2,-3,-4,-5,-5,-7,-8,-9,-10])
    tests.append([1.5,2.2,3.6,4.3,5.7,6.4,7.2,8.1,9.5,10.0])

    for test in tests:
        assert find_median.find_median(test) == statistics.median(test), f'Hmm...your find_median function failed my test: {find_median.find_median(test)} is not the median value in {test}.'

test_median
