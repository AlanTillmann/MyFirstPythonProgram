#print('Hello world!')

'''
Variables
x = 1
y = x
y += 1
z = x + y
print(z)

Concatenation
greeting = 'Hello '
fName = 'TheRealBreezy_01 '
lName = 'Boi'
print(greeting + '' + fName + '' + lName)

Arrays and Input
array = []
elem = input()
array.append(elem)
print(array)
array.append(0)
print(array)
array.pop()
print(array)

In function for searching array
char = 'A'
array = ['A', 'B', 'C']
if char in array:
    print('char was found')

While Loop
done = False
while (not done):
    print('Enter Q to quit.')
    x = input()
    if x == 'Q' or x == 'q':
        done = True

For Loop
for x in range(10):
    print(x)

For Loop w/ Array
array = ["Jan", "Feb", "March", "April", "May"]
for i in array:
    if i != 'April':
        print(i)

Functions
def add(x,y):
    z = x + y
    return z

def outputAdd(x1,y1):
    print(add(x1,y1))

outputAdd(2,2)

Boolean Array Function
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def isInList(num):
    if num in array:
        return True
    else:
        return False

print(isInList(1))
'''

done = False
array = []
def mainMenu():
    global done
    print('---------------------')
    print('       Main Menu')
    print('---------------------')
    print('[1] View list')
    print('[2] Add to list')
    print('[3] Remove from list')
    print('[4] Quit')
    print('>>')
    text = input()
    if (text == '1'):
        viewList()
    elif (text == '2'):
        addToList()
    elif (text == '3'):
        removeFromList()
    elif (text == '4'):
        done = True
    else:
        print('Invalid input you fool!')

def isEmpty():
    if array == []:
        return True

def viewList():
    if isEmpty():
        print('The list is empty stinky.')
    else:
        print('This list contains the following: ')
        for x in array:
            print(x)
        #print(array)

def addToList():
    print('Enter a value: ')
    user = input()
    array.append(user)

def removeFromList():
    array.pop()

while done != True:
    mainMenu()















