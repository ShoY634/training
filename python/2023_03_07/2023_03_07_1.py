def makenumlist(start, end):
    numlist = []
    
    while start <= end:
        tuple1 = (start, start+1)
        numlist.append(tuple1)
        start += 1
    
    return numlist
    
print(makenumlist(1, 10))
