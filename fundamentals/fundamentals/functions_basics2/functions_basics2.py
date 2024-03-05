#Countdown

def countdown(x):
    L=[]
    for i in range(x,-1,-1):
        L.append(i)
    return L 
print(countdown(5))

#Print and Return
def print_and_return(L):
    print(L[0])
    return(L[len(L)-1])

print(print_and_return([1,2,3,4,5,6]))

#First Plus Length

def first_plus_length(L):
    return L[0]+len(L)
print(first_plus_length([2,5,6,7]))
print(first_plus_length([1,2]))

#Values Greater than Second
def greater_than_second(L):
    X=[]
    for i in range(0,len(L)-1):
        if L[i]>L[i+1]:
            X.append(L[i])
    print(len(X))
    if len(L)<=2:
        return False
    else:
        return X 
print(greater_than_second([7,6,5,4,3]))
        

#This length; That value

def length_value(n,m):
    L=[]
    for i in range(0,n):
        L.append(m)
    return L 
print(length_value(2,7))
print(length_value(7,2))






