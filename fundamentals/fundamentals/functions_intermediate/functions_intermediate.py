
#1 
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15
print(x)

students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30


#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionnary(liste):
    for i in range(0,len(liste)):
        for data in  liste[i] : 
            print(data, "-", liste[i][data])
        
print(iterateDictionnary(students))

#3 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name,some_liste):
    for i in range(0,len(some_liste)): 
        for key,val in some_liste[i].items():
            if key == key_name:
                print(val)

print(iterateDictionary2('first_name', students))

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key,val in some_dict.items():
        print(len(val), key)
        for i in range(0,len(val)):
            print(val[i])

print(printInfo(dojo))





