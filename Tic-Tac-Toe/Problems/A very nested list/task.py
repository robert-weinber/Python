str_1 = input()
str_2 = input()
str_3 = input()
my_list = [str_1]
my_list.append([])
my_list[1].append(str_2)
my_list.append([])
my_list[2].append([])
my_list[2][0].append(str_3)
print(my_list)