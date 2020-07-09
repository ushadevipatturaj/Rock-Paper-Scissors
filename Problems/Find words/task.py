user_list = input().split()
temp = []
for i in user_list:
    if i.endswith('s'):
        temp.append(i)
print("_".join(temp))