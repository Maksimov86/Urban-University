my_dict = {
    "name": "Slava",
    "Year of birth": 1986
}

print(my_dict["name"])

new_dict = {
    'city': 'New York',
    'a': 1,
    'd': 4
}
my_dict.update(new_dict)

del my_dict["city"]
print(my_dict)

my_set = {1, "hi", 3, 1, "hi", True, True, 5.6}
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([23, "Putin"])
print(my_set)
my_set.remove(5.6)
print(my_set)