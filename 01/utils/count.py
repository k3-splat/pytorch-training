def count_char(s, c):
    n = 0

    for i in s:
        if c == i:
            n = n + 1
    
    return n