#basic

for i in range(0,151):
    print(i)

#Multiples of Five

for i in range(5,1001):
    if i%5==0 :
        print(i)

#Counting the dojo way 

for i in range(1,101):
    if i%10 ==0 :
        print("Coding Dojo")
    elif i%5 == 0 :
        print("Coding")
    else :
        print(i)

#Whoa That Sucker's Huge

sum = 0
for i in range(0,500001):
    if i%2!=0 :
        sum = sum + i

print(sum)

#Countdown by four 

for i in range(2018,0,-4):
    print(i)  

#Flexible Counter

lowNum=0
highNum=20
mult=10
for i in range(lowNum,highNum+1):
    if i%mult==0 : 
        print(i)
