text = input()
words = text.split(' ')

for _word in words:
    # finish the code here
    temp = _word.lower()
    if temp.startswith('https://') or temp.startswith('http://') or temp.startswith('www.'):
        print(_word)
