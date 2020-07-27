print([1,2,3])
print([1,['hello',4.45],4,'dear'])
for i in [1,2,3,4,5,]:
    print(i)
print('Done')
fndlist =['i','me','mein']
for fnd in fndlist:
    print('HBD',fnd)
print('done')
fruit ='mango'
print(fruit[1])
f=fruit.upper()
print(f)
numbers= [1,2,3,4,5,6,7,8,9]
numbers[0]=10
print(numbers)
print(len(fndlist))
print(range(len(fndlist)))
addList=fndlist+numbers
print(addList)
print(numbers[1:3])
favouriteBooks= list()
favouriteBooks.append('Masud rana')
favouriteBooks.append('Bristi Bilas')
favouriteBooks.append('Deyal')
print(favouriteBooks)
'Deyal'in favouriteBooks
favouriteBooks.sort()
print(favouriteBooks)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print("Average:",(sum(numbers))/len(numbers))



numList =list()
while True:
    inpNum =input('Enter Number:')
    if inpNum == 'done':break
    value = float(inpNum)
    numList.append(value)

average =sum(numList)/len(numList)
print(average)


randomStr ='why always me'
splitStr =randomStr.split()
print(splitStr)
for words in splitStr:
    print(words)


rawData = 'From ta7890@diu.edu.bd 7:30pm Sat 1/30/2020'
split1 = rawData.split()
email = split1[1]
print(split1[3])
split2 = email.split('@')
org =split2[1]
print(org)





