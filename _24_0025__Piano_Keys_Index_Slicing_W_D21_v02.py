# Index Slicing:
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
        #      |    |    |    |    |    |    |    |
     #  Index: 0    1    2    3    4    5    6    7

print(piano_keys[2:5])
# ['c', 'd', 'e']


print(piano_keys[2:])
# ['c', 'd', 'e', 'f', 'g']


print(piano_keys[:5])
# ['a', 'b', 'c', 'd', 'e']


print(piano_keys[2:5:2])  #3rd number is the Incremental step
# ['c', 'e']


print(piano_keys[::2])    #everything in the List, but I only want every other item
# ['a', 'c', 'e', 'g']


print(piano_keys[::-1])   #reverses the entire list, in backwards order!
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])                                 #it can also slice Tuples!
# ('mi', 'fa', 'so')
