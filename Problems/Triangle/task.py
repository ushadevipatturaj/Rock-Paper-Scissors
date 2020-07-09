input_str = int(input())
for i in range(input_str):
    string_val = '#' * ((i * 2)+1)
    x = string_val.center(input_str*2, ' ')
    print(x)
    #print(str.center(input_str*2, string_val))