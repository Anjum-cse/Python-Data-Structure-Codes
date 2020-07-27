purse = dict()
purse['anjum']=12
purse['veer']=10
purse['rumy']=5
print(purse)
purse['veer']=10 -7
print(purse)
purse['atm']=2
print(purse)
purse['anjum']=10
print(purse)
print(list(purse))
print(purse.keys())
print(purse.values())
print(purse.items())

for key in purse:
    print(key,purse[key])
for a,b in purse.items():
    print(a,b)



counts= dict()
names=['i','me','or','mein','i','you','mein','i']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)



countWord =dict()
line = input("Enter a line:")
wordsInLine= line.split()
print("Words:",wordsInLine)
for word in wordsInLine:
    countWord[word]=countWord.get(word,0)+1
print("Counts:",countWord)


