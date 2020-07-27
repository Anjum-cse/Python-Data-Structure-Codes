fname = input("Enter file name: ")
fh = open(fname).read()
wordsinfile =fh.split()
print(wordsinfile)
counts = dict()
bigWord= None
bigCount=None
for word in wordsinfile:
    counts[word]=counts.get(word,0)+1
print(counts)
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount=count
        bigWord=word
print(bigWord,bigCount)

lst =list()
for (key,value) in counts.items():
    newtup=(key,value)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for (key,value) in lst[:10]:
    print(key,value)
