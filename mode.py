import numpy as np

array = np.array([1, 2, 1, 2, 3, 4, 5, 6, 8, 9, 1, 2, 2, 22, 21, 1, 1, 1, 1, 2, 5])

number_counts = {}

for num in array:
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1
        
number_with_max_count = max(number_counts.values())

mode = [key for key, count in number_counts.items() if count == number_with_max_count]

print("Original Array:\n", array)
print("\nCount of Numbers:\n", number_counts)
print("\nMode:\n", mode)
print("\nCount of Mode:\n", number_with_max_count)

import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1)
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")
li2[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")