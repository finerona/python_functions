
def checknumber(x):
    if x % 2 == 0 and x < 10:
        print(' the number is even and less than 10')
    else:
        print('the number is odd')


checknumber(9)
def checksum(a,b):
    sum = a + b
    print(sum)

checksum(5,5)
def addnumbers(a,b):
    sum = a + b
    print(sum)

addnumbers(20,20)

def checkage(dateofbirth,currentyear):
    age = dateofbirth - currentyear
    print(age)

checkage(2024,1997)

def stateandcapital(state):
    states = {
        "ikeja" : "Lagos",
        "Edo" : "Benin",
        "Abuja" : "FCT" 

    }
    for keys, values in states.items():
        if keys == state:
            capital = values
            print(f'the capital of {state} is {capital}')
stateandcapital('Edo')

def multiplication(x,y):
    mul = x * y
    print(mul)

multiplication(5,5)

def Division(r,t):
    div = r / t
    print(div)
Division(10,2)

a = 10
b = 20
if a > b:
    print('a is greater than be')  
elif a == b:
     print('a equals to b')
else:
    print('b is greater than a')