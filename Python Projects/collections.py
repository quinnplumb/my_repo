# lists
lst = [10, 20, 30, 40, 50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)
lst.pop(2)
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst.reverse()
print(lst)
lst.reverse()

lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)

lst.append(20)
lst.append(20)
lst.append(20)
print(lst)

count20 = lst.count(20) # helpful for hw2
print(count20)

copy_lst = lst
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst) # changing copy_lst will also change the original lst (copies the memory address)

new_copy = lst.copy() # this method creates a new memory address and you can edit each individual list
new_copy[0] = 55
print(lst)
print(new_copy)

new_copy = lst[:]
print(new_copy)

# for loops
empt_list = []
for o in lst:
    empt_list.append(o)
print(empt_list)

empt_list = [0] * 10
print(empt_list)
empt_list[0] = 10
print(empt_list)

"""
List Comprehension
 - A compact programming expression used to create a list based on a sequence such as a range, string, or another list
 ex: squaring numbers in a range
"""
squares = []
for i in range(1,10):
    squares.append(i*i) # basic way to do this
print(squares)

squares = [x * x for x in range(1, 10)] # Comprehensive way to do this
print(squares)

plus_5 = [x + 5 for x in lst]
print(plus_5)

# Comprehension Filters
small_vals = [x for x in lst if x < 20]
print(small_vals) # returns all values in the original list less than 20

"""
Dictionaries:
 - A dictionary is a data structure used to map a set of keys to their values
    - common use cases:
        1. Look up values
        2. Count occurences
        3. Store a record of related values
    - keys must be unique. Duplicates are not allowed.
"""
fav_foods = {"Kathleen" : "pizza", "Quinn" : "steak", "Kush" : "fries",
              "Hannah" : "pasta", "Yamill" : "fries"}
print(fav_foods)

hff = fav_foods["Hannah"]
print(hff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}") # f makes imbedded strings work

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}.")


if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print (fav_foods)