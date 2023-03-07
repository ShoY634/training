def count_snacks(money):
    B = C = D = 0
    
    if money < 150:
        a = b = c = d = 0
        A = 0
        
    elif 150 <= money < 300:
        a = 1
        b = c = d = 0
        A = 1
        
    elif 300 <= money < 450:
        b = 1
        a = c = d = 0
        A = 2
        
    elif 450 <= money < 600:
        c = 1
        a = b = d = 0
        A = 3
    
    elif 600 <= money <750:
        d = 1
        a = b = c = 0
        A = 4
    
    else:
        d = money//600
        c = (money - d * 600)//450
        b = (money - d * 600 - c * 450)//300
        a = (money - d * 600 - c * 450 - b * 300)//150
        A = money//150
        
        
    quantity_min = "min : " + str([a, b, c, d])

    quantity_max = "max : " + str([A, B, C, D])
    
    return quantity_min, quantity_max


result = count_snacks(950)
print(result[0])
print(result[1])