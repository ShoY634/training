# ＊実行結果を直下のコメントに表示しています＊

list_name = ['Alice', 'Bob', 'Charlie']
list_race = ['White', 'Brack', 'Yellow']
list_id = [1, 2, 3]
list_age = [20, 50, 40]

dict_name = {name:len(name) for name in list_name}
print(dict_name)
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

list_profile = {name:race for name, race in zip(list_name, list_race)}
print(list_profile)
# {'Alice': 'White', 'Bob': 'Brack', 'Charlie': 'Yellow'}

dictlist_profile = [{name:race} for name, race in zip(list_name, list_race)]
print(dictlist_profile)
# [{'Alice': 'White'}, {'Bob': 'Brack'}, {'Charlie': 'Yellow'}]

dictlist_profile2 = [{'id':id, 'name':name, 'race':race, 'age':age} for id, name, race, age in zip(list_id, list_name, list_race, list_age)]
print(dictlist_profile2)
# [{'id': 1, 'name': 'Alice', 'race': 'White', 'age': 20}, {'id': 2, 'name': 'Bob', 'race': 'Brack', 'age': 50}
# , {'id': 3, 'name': 'Charlie', 'race': 'Yellow', 'age': 40}]

list_age_sorted = []
for i in dictlist_profile2:
    print(f"{i['id']} {i['name']}")
    # 1 Alice
    # 2 Bob
    # 3 Charlie
    list_age_sorted.append(i['age'])
    
print(list_age_sorted)
# [20, 50, 40]

list_age_sorted.sort()
print(list_age_sorted)
# [20, 40, 50]
