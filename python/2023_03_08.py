# for i in range(10):
#     print(i)
    
# list = ["Apple", "Orange", "Banana", "Grape"]

# for name in list:
#     if name == "Banana":
#         break
#     print (name)


# for name in list:
#     if name == "Banana":
#         print("monkey")
#         continue
#     print(name)
    
    
# for name in list:
#     print(name)

# else:
#     print("end")
    
    
# count = 0
# for name in list:
#     if count == 3:
#         break
    
#     print(name)
#     count += 1

# else:
#     print("I'm full stomach")
    
    
# for i in range(5, 20, 3):
#     print(i)
    

# for i, name in enumerate(list):
    # print("index:" + str(i), name)
    # print(f"index: {str(i)} {name}")

# for name in enumerate(list, 1):
#     print(name)
    
# for _, name in enumerate(list):
#     print(name)
    
# dictionary = {}
# for i, name in enumerate(list, 1):
#     dictionary[i] = name
    
# print(dictionary)
# ------------------------

list_taste = ["toobad", "good", "excelent", "normal"]


# for name, taste in zip(list, list_taste):
#     print(name, taste)

# ---------------------------------------------

list_cost = [100, 150, 50, 200]


# for name, taste, cost in zip(list, list_taste, list_cost):
#     print(f"{name} taste:{taste} cost:{cost}yen")
    
# -----------------------------------------------

# squares = [i**2 for i in range(5)]
# print(squares)

# odds = [i for i in range(10) if i % 2 == 1]
# print(odds)

# multiple3 = [i*3 for i in range(10)]
# print(multiple3)

# odd_even = ["odd" if i % 2 == 1 else "even" for i in range(10)]
# print(odd_even)

# nabeatsu = [i for i in range(50) if not i % 3 == 0]
# print(nabeatsu)

# --------------------------------

list_ramen = ["syoramen", "tyuramen", "dairamen", "tokudairamen"]
list_ramen_cost = [100, 150, 300]

# menu = {}
# for ramen, cost in zip(list_ramen, list_ramen_cost):
#     menu[ramen] = cost
    
# print(menu)

def ramen_menu(namelist, costlist):
    menu = {}
    while True:
        if len(namelist) > len(costlist):
            costlist.append(1000)
            costlist = costlist + [1000]
            
        else:
            len(namelist) == len(costlist)
            break
    
    for name, cost in zip(namelist, costlist):
        menu[name] = cost
        
    return menu

# print(ramen_menu(list_ramen, list_ramen_cost))

# -------------------------------------------------

menu = {'syoramen': 100, 'tyuramen': 150, 'dairamen': 300, 'tokudairamen': 1000}

print(menu.values())
a = menu.values()
menu_values_list = list(menu.values())
print(menu_values_list)