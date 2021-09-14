import string
handle = open("/resources/wordfile.txt", 'r')
counts=dict()
for line in handle:
    words = line.split()
    for word in words:
        for p in string.punctuation:
            if p in word:
                word = word.replace(p,'')
        counts[word]=counts.get(word, 0)+1
print(counts)
bigword=None
bigcount=None
order=dict()
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigcount=count
        bigword=word
print(bigword, bigcount)
