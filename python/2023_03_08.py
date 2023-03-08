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
#     print("index:" + str(i), name)

# for name in enumerate(list, 1):
#     print(name)
    
# for _, name in enumerate(list):
#     print(name)
    
dictionary = {}
for i, name in enumerate(list, 1):
    dictionary[i] = name
    
print(dictionary)