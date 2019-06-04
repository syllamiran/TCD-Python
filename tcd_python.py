import pandas as pd
import numpy as np
import sys



df = pd.read_excel('C:\data4.xlsx')
print("\n")
print("Welcome to my dynamic cross table with the excel file:\n ")


data = list(df.columns)
dataLength = len(data)

print("\nYou have ", dataLength, " columns in your file :")
for col in df.columns:
    print(col)

print('\n')

def options(argument):
    switcher = {
            1: ("Your choice : VIEW ONLY FIELD "),
            2: ("Your choice : SORT BY " ),
            3: ("Your choice : VIEW CUSTOM COLUMN"),
            4: ("Your choice : VIEW SUM OF CUSTOM COLUMN"),
            5: ("Thank you foe testing my application. Bye Bye")
    }

    return switcher.get(argument, "Bye Bye")


def menu_choice():
    print("Menu:")
    print("1 - VIEW ONLY FIELD")
    print("2 - SORT FIELD BY")
    print("3 - VIEW CUSTOM COLUMN")
    print("4 - ADDITION CUSTOM COLUMN")
    print("5 - QUIT APPLICATION \n")
    choice = input("Your choice (1 - 2 - 3 - 4 - 5 : > ")
    argument = int(choice)
    print(options(argument))
    return choice

def view_only():
    print("\n")
    for col in df.columns:
        print("Field:", col)
    print("\n")
    choice = input("\n> Select the field to view : >")
    choiceData = choice.split()
    if choiceData[0-1] in data:
        for i in data:
            if choice == i:
                values = df[str(choice)].value_counts()
                print(values, '\n')
                print("You have " , len(values), " entry(ies) for the field : ", str(choice),  '\n' )
                choiceExit = input('Enter 0 to go back to menu or 1 to continue: > \n')
                if choiceExit == "0":
                    main()
                elif choiceExit == "1":
                    view_only()

    else :
        print ("\nERROR... Please enter a true data field. Thank you! \n")
        view_only()

def sort_by():
    print("\n")
    for col in df.columns:
        print("Field:", col)
    print("\n")
    choice = input("\n> Select the field to sort : >")
    choiceData = choice.split()
    if choiceData[0-1] in data:
        for i in data:
            if choice == i:
                values = pd.pivot_table(df,index=[str(choice)])
                print(values, '\n')
                choiceExit = input('Enter 0 to go back to menu or 1 to continue: > ')
                if choiceExit == "0":
                    main()
                elif choiceExit == "1":
                    sort_by()
    else :
        print ("\nERROR... Please enter a true data field. Thank you! \n")
        sort_by()

def columnView():
    print("\n")
    for col in df.columns:
        print("Field:", col)
    print("\n")
    col_nbr = input("Enter the NUMMBER of columns to show : > ")
    int_nbr = int(col_nbr)
    if int_nbr >= dataLength:
        print("\nERROR. Please enter a number less or equal ", (dataLength),  "\n")
        columnView()
    else:
        print('You have choosen ' , int_nbr , 'index. enter(s) it now :' )
        value = input("Enter a list element separated by space ")
        listData = value.split()
        lenData = len(listData)
        if lenData == int_nbr:
            if listData[0-1] in data:
                print(df[listData], '\n')
                choiceExit = input('Enter 0 to go back to menu or 1 to continue: > ')
                if choiceExit == "0":
                    main()
                elif choiceExit =="1":
                    columnView()
            else:
                print ("\nERROR... Please enter a true data field(s). Thank you! \n")
                columnView()
        else :
            print("\nERROR... Please enter a true data field(s) ",(int_nbr), '\n')
            columnView()

def columnSum():
    print("\n")
    for col in df.columns:
        print("Field:", col)
    print("\n")
    indexShow = input("Enter the NUMBER of index : > ")
    indexToShow = int(indexShow)
    if indexToShow >= dataLength:
        print("\nERROR... Please enter a number less or egal ", (dataLength)," \n")
        columnSum()
    else:
        print('You have choosen ' , indexToShow , 'index. enter(s) it now :' )
        value = input("Enter a list index separated by space ")
        listData = value.split()
        lenData = len(listData)
        if lenData == indexToShow:
            valueSum = input("Enter the values to sum : >")
            sumData  = valueSum.split()
            if listData[0-1] and sumData[0-1] in data:
                result = pd.pivot_table(df, index=listData, values=sumData, aggfunc=np.sum)
                print(result, '\n')
                choiceExit = input('Enter 0 to go back to menu or 1 to continue: > ')
                if choiceExit == "0":
                    main()
                elif choiceExit =="1":
                    columnSum()
            else:
                print ("\nERROR... Please enter a true data field(s). Thank you! \n")
                columnSum()
        else :
            print("\nERROR... Please enter a true data field(s) ",(indexToShow))
            columnSum()

def appExit():
    sys.exit()


def main():
    choice = menu_choice()
    if str(choice) == "1":
        view_only()
    elif str(choice) =="2":
        sort_by()
    elif str(choice) == "3":
        columnView()
    elif str(choice) == "4":
        columnSum()
    elif str(choice) == "5":
        appExit()


if __name__ == '__main__':
    main()

