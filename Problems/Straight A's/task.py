# put your python code here
str_input = input()
str_list = str_input.split()
print(round(str_list.count('A') / len(str_list), 2))