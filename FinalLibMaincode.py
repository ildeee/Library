from FinalLibSubcode import *
from ReadAndWrite import write_Book,write_User

        

print( "Welcome to Sample Library" )
print( "Press Enter ")
input()

#First Loop
option = 1

while option < len(user_dict)+2:
    mainMenu()
    print()
    option = int(input())
    print()       

    #Creating new user
    if option == len(user_dict)+1:  
            user_make()
            option = option + 1

    #Continuing...
    elif option in range (1 ,len(user_dict)+1):
        print(" Enter Password ")
        password = input()

        #Checking Password
        if password == user_dict [option-1] ['Password']:
            print("Welcome" , user_dict [option-1] ['User'])

            #Login User - Librarian
            if user_dict [option-1] ['User']=='Librarian':
                choice = 0

                while choice!=4 :
                    librarianMenu()
                    print()
                    choice = int(input())
                    option_Func(choice)[choice]()


            #Login User - Others
            else:
                choice = 0
                while choice != 6 :
                    print()
                    membersMenu()
                    print()
                    choice = int(input())
                    print()

                    option_Func_User(option)[choice](option)
                    
write_Book('bookData.dat', inventory_dict)
write_User('userData.dat',user_dict)
    
