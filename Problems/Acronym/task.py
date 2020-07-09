# read test.txt
test_file = open('test.txt', 'r')
for line in test_file.readlines():
    print(line[0])
test_file.close()