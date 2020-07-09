input_list = input().split()
temp = []
for i in input_list:
    if input_list.index(i) == 0:
        temp.append(i.lower())
    else:
        temp.append(i.title())
print("".join(temp))