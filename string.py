
data = "from tanvir15-7890@diu.edu.bd.com sat 5.30"
startSearch= data.find('@')
print(startSearch)
endSearch= data.find(' ',startSearch)
print(endSearch)
orgFrom= data[startSearch+1 : endSearch]
print(orgFrom)


