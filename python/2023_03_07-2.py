def makenumlist(start, end):
    numlist = []
    
    while start <= end:
        tuple1 = (start, start+1)
        
        if start % 3 == 0:
            start += 1
            continue
        
        numlist.append(tuple1)
        start += 1
        
    
    return numlist
    
print(makenumlist(1, 10))