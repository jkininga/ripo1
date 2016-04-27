def sum_of_digits(A):
    '''
        Takes a list A, and returns the sum of all 
        digits in the list e.g. [10, 20,45] should
        return 1 + 0 + 2 + 0 + 4 + 5 = 12
    '''
    total = 0
    base = 10
    newlist = []

    for a in A:
        while a > 0:        
            newlist.append(a % base)
            a //= base
    for b in newlist:
        total += b
    return total



print sum_of_digits([10, 20,45])

