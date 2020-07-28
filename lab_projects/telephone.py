from database import Simpledb
loop=True
db = Simpledb('telephone.txt')
db.__repr__()
while loop==True:
    print('Would you like to:\n1:Delete a phone number?\n2:Update a phone number?\n3:Add another phone number?\n4:Find a phone number?\n5:Quit the program\nEnter a number 1-5')
    choice=input()
    while choice!='1' and choice!='2' and choice!='3' and choice!='4' and choice!='5':
        print('Please type 1, 2, 3, 4, or 5.')
        choice=input()
        if choice=='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5':
            break
    if choice=='1':
        print('Whose number would you like deleted (enter a name)')
        name=input()
        db.delete(name)
        print('Number is deleted.')
    if choice=='2':
        print('Whose number would you like to update?')
        name=input()
        print('What number would you like to update with?')
        number=input()
        db.update(name,number)
    if choice=='3':
        print('What number would you like added?')
        number=input()
        print('Whose number is it?')
        name=input()
        db.add(name,number)
    if choice=='4':
        print('Whose number is it?')
        name=input()
        db.find(name)
    if choice=='5':
        loop=False