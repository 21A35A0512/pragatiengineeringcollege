'''
for i in range(1,10):
    print(i)
for i in range(1,10):
    print(i,end="*")

for i in range(10,0,-1):
    print(i,end="*")


for i in range(97,123):
    print(chr(i),end=" ")



for i in range(122,96,-1):
    print(chr(i),end=" ")


for i in range(65,91):
    if(i==65 or i==69 or i==73 or i==79 or i==85):
        print(chr(i),end=" ")



for i in range(65,91):
    if(i!=65 or i!=69 or i!=73 or i!=79 or i!=85):
        print(chr(i),end=" ")


for i in range(91,65,-1):
    if(i!=65 or i!=69 or i!=73 or i!=79 or i!=85):
        print(chr(i),end=" ")

package=84
data=float(2.0)
calls=3000
msg=100
a=int(input("enter the day:"))
if(a<=84):
    b=int(input("enter the calls:"))
    c=int(input("enter the messeges:"))
    d=float(input("enter the data:"))
    print("your plan will expire in ",84-a,"days")
else:
    print("your plan expired")

for i in range(1,155):
    if(i%10==0):
        print(i)
       
for i in range(1,30):
    if(i%2==1 and i<=5):
        print(i*5)
        
for i in range(1,30):
    if(i%2==1):
        print(i*5)

for i in range(-10,-1,2):
    print(i)
    

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
    
for i in range(1,11):
    print(i,"*10=",i*10)
    '''
rows=5
i=1
while i<=rows:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print(" ")
  
