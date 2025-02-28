from hw2_debugging import merge_sort

def test_merge1():
    assert merge_sort([2,5,2,7,12,16,11,11,11,6,7,7,9,10,17,13,4,5,9,13]) == [2, 2, 4, 5, 5, 6, 7, 7, 7, 9, 9, 10, 11, 11, 11, 12, 13, 13, 16, 17]

def test_merge2():
    assert merge_sort([4,7,8,8,9,12,14,11,16,2,16,1,7,18,19,10,3,6,2,8]) == [1, 2, 2, 3, 4, 6, 7, 7, 8, 8, 8, 9, 10, 11, 12, 14, 16, 16, 18, 19]

def test_merge3():
    assert merge_sort([19,19,19,19,19,3,5,2,11,11,1,4,5,5,5,5,6,12,18,19]) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 11, 11, 12, 18, 19, 19, 19, 19, 19, 19]
