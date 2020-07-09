# read sample.txt and print the number of lines
sample = open('sample.txt', 'r')
total_lines = 0
for line in sample:
    total_lines += 1
print(total_lines)
sample.close()