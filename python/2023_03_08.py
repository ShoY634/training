# for i in range(10):
#     print(i)
    
list = ["Apple", "Orange", "Banana", "Grape"]

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

squares = [i**2 for i in range(5)]
print(squares)

odds = [i for i in range(10) if i % 2 == 1]
print(odds)

multiple3 = [i*3 for i in range(10)]
print(multiple3)

odd_even = ["odd" if i % 2 == 1 else "even" for i in range(10)]
print(odd_even)

nabeatsu = [i for i in range(50) if not i % 3 == 0]
print(nabeatsu)