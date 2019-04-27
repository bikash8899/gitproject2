inp = input('Enter file name: ')
fhand = open(inp)
counts = {}
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    
for k,v in sorted(counts.items()):
    print(k,v)