def heading(word, hash_str=1):
    if hash_str <= 1:
        return '# ' + word
    elif hash_str > 6:
        return '###### ' + word
    else:
        return ('#' * hash_str) + ' ' + word
