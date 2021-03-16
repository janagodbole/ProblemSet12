number_list = [5,3,7]
print("negative")
number_list[0] = number_list[0] * -1
[print(number_list)]

print("10 added")
number_list.append(10)
print(number_list)

print("16 @ 2")
number_list = number_list[0:2] + [16] + number_list[2:]
print(number_list)

print("letter @ 1 removed")
number_list.remove(number_list[1])
print(number_list)

print("temporarily sorted number list")
print(sorted(number_list))
print("Now the list is back to normal")
print(number_list)

print("sort list permanently")
number_list.sort()
print(number_list)

print("Now I will change all the even numbers in the data list \n"
      "to negative numbers")

k = 0
for k in range(len(number_list)):
    i = number_list[k]
    if i % 2 == 0:
        i = i * -1
        number_list[k] = i
        k = k + 1
    else:
        k = k + 1
print(number_list)

print("Here are the negative numbers in their own data list")
k = 0
negative_number_list = []
for k in range(len(number_list)):
    i = number_list[k]
    if i < 0:
        negative_number_list.append(i)

        k = k + 1
    else:
        k = k + 1
print(negative_number_list)

print("Here is a list of all of the numbers")
sum_list = []
k = 0
while k < len(number_list):
    sum_list.append(number_list[k])
    k += 1

a = 0
while a < len(negative_number_list):
    sum_list.append(negative_number_list[a])
    a += 1
print(sum_list)

help(sum_list)