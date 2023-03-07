def make_num_list(start, end):
    num_list = []
    
    while start <= end:
        tuple1 = (start, start+1)
        
        if start % 3 == 0:
            start += 1
            continue
        
        num_list.append(tuple1)
        start += 1


    return num_list

    
def make_num_list_imp(start, end):
    num_list2 = []
    
    while start <= end:
        tuple2 = (start, start+1)
        
        if start % 3 == 0 or (start + 1) % 3 == 0:
            start += 1
            continue
        
        num_list2.append(tuple2)
        start += 1


    return num_list2

    
print(make_num_list(1, 10))
print(make_num_list_imp(1, 10))