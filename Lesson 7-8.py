from random import randist
lst = [randist (-10,10) for i in range (20)]
print(lst)

sum_negetive = 0


for num in lst:
    if num < 0: sum += num
print("Sum negative item list:", sum_negative)



sum_of_even = 0