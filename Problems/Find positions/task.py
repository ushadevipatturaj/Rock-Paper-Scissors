# put your python code here
seq_str = input()
seq_list = seq_str.split()
lookup = input()
count = 0
find_list = ''
for i in seq_list:
    if i == lookup:
        find_list += str(count)+' '
    count += 1
if len(find_list) == 0:
    print("not found")
else:
    print(find_list.strip())