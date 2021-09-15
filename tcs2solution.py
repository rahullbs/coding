def word_count(str):
    counts = dict()
    l=[]
#     print(counts)
    words = str.split()
#     print(words)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
#     return counts
    for key in counts:
        if counts[key] > 1:
            l.append(key)
    return l