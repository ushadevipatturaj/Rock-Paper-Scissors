input_list = input().split("_")
temp = (i.title() for i in input_list)
print("".join(temp))