def heading(word, hash=1):
    if hash <= 1:
        return '# '+word
    elif hash > 6:
        return '###### '+word
    else:
        return ('#' * hash)+' '+ word
