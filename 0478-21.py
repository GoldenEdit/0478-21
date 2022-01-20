from tabulate import tabulate
Areas = ['the pier entrance gate', 'the gift shop', 'painting and decorating']
Options = ['Members who have chosen to work as volunteers.','Volunteers who would like to work at the pier entrance gate','Volunteers who would like to work in the gift shop.','Volunteers who would like to help with painting and decorating tasks','Members whose membership has expired (they have not re-joined this year).','Members who have not yet paid their $75 fee.']
userNames = ['John Smith','Jane Smith']
wishToWork = ['Y','N']
userArea = ['the pier entrance gate','the gift shop']
userDate = ['01/01/2022','06/01/2022']
userFee = ['Y', 'N']
userPlank = ['N','Y']
userPlankMessage = ['Wow a plank of wood!','hi im wood']
def main():
    indb = len(userNames)
    print (indb)
    print('==  Friends of Seaview Pier ==')
    names = input('Please enter your first and last name: ')
    userNames.append(names)
    #wishToWork = input('Would you like to work as a volunteer? Y/N')
    wishToWork.append('Null')
    while wishToWork[indb] != 'Y' and wishToWork[indb] != 'N':
        wishToWork[indb] = input('Would you like to work as a volunteer? Y/N: ')
        if (wishToWork[indb] == 'Y'):
            #   Area  
            area = 10
            printAreas()
            while area < 0 or area > 2:
                area = int(input('Which area do you want to work at? Please give the ID: '))
                userArea.append(Areas[area])

            userDate.append(input('Please enter the date today, DD/MM/YYYY: '))
            
            userFee.append('Null')
            while userFee[indb] != 'Y' and userFee[indb] != 'N':
                userFee[indb] = input('Did you pay the 75$ fee? Y/N: ')
      

        elif (wishToWork[indb] == 'N'):
            print('valid')
            userDate.append(input('Please enter the date today, DD/MM/YYYY: '))
            
            userFee.append('Null')
            while userFee[indb] != 'Y' and userFee[indb] != 'N':
                userFee[indb] = input('Did you pay the 75$ fee? Y/N: ')
            
        else:
            print('Not valid')

    goodInput = False
    userPlank.append('Null')
    while goodInput != True:
        while userPlank[indb] != 'Y' and userPlank[indb] != 'N':
            userPlank[indb] = input('Would you like to sponsor a wooden plank? Y/N: ')
        if userPlank[indb] == 'Y':
            userPlankMessage.append('Null')
            userPlankMessage[indb] = input('Short message to be on the plank: ')
            inputOkay = 'Null'
            while inputOkay != 'Y' and inputOkay != 'N':
                inputOkay = input('Your message is: "' + userPlankMessage[indb] + '" is this okay? Y/N: ')
            if inputOkay == 'N':
                goodInput = False
            else:
                goodInput = True
    
    printOptions()

    option = input('Please enter the ID of the query you would like to make: ')

    if option == '0':
        x=0
        for i in wishToWork:
            if i == 'Y':
                print(userNames[x])
            x=x+1
    elif option == '1':
        x=0
        for i in userArea:
            if i == 'the pier entrance gate':
                print(userNames[x])
            x=x+1
    elif option == '2':
        x=0
        for i in userArea:
            if i == 'the gift shop':
                print(userNames[x])
            x=x+1
    elif option == '3':
        x=0
        for i in userArea:
            if i == 'painting and decorating':
                print(userNames[x])
            x=x+1
    elif option == '4':
        x=0
        for i in userDate:
            if '2022' not in userDate[x]:
                print(userNames[x])
            x=x+1
    elif option == '5':
        x=0
        for i in userFee:
            if i == 'N':
                print(userNames[x])
            x=x+1
    else:
        print('Not Valid')

    




    













def printAreas():

    data = []
    for i in range(0, len(Areas)):
        data.append([i, Areas[i]])
    print(tabulate(data, headers=["ID", "AREA"], tablefmt = "fancy_grid", numalign="right"))
    print("")

def printOptions():
    data = []
    for i in range(0, len(Options)):
        data.append([i, Options[i]])
    print(tabulate(data, headers=["ID", "OPTION"], tablefmt = "fancy_grid", numalign="right"))
    print("")





# KEEP
if __name__ == '__main__':
    main()