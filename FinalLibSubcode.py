from ReadAndWrite import read_Lib,read_User

user_dict = read_User('userData.dat')
inventory_dict = read_Lib('bookData.dat')


#Librarians help thing
def book_Entry(Title , Author , Genre , Year , Publisher):
    
    '''This allows librarian to insert new data into table'''
    
    inventory_dict.insert(-1, {'Title' : Title ,
                          'Author' : Author,
                          'Genre' : Genre ,
                          'Year' : Year ,
                          'Publisher' : Publisher,
                          'Borrowed' : None})
    return inventory_dict

#To create a new user
def new_user ( Username , Password):
    
    '''Allows to enter a new user login'''
    
    return user_dict.insert(-1 ,{'User' : Username ,
                                 'Password' : Password , 'Current' :''})

#Main-Menu
def mainMenu():
    '''Views first Menu'''
    print(" Please Choose login ID")
    for i,user in enumerate(user_dict):
        print(f'{i + 1} ) {user["User"]}')
    print(f'{len(user_dict)+ 1} ) Create Login')
    print(f'{len(user_dict)+ 2} ) Quit')
    print("Enter selected option")


#Librarian-Menu
def librarianMenu():
    '''Views Librarian Menu'''
    print(' Choose appropriate option\n',
          '0 ) View all books\n',
          '1 ) View all users\n',
          '2 ) Add new books\n',
          '3 ) View all borrowed books and who borrowed them\n',
          '4 ) Log Out\n')

#Members-Menu
def membersMenu():
    '''Views Members menu'''
    print(' Choose appropriate option\n',
          '0 ) View all books\n',
          '1 ) View all available books\n',
          '2 ) Search books based on criteria\n',
          '3 ) Show books currently reading\n',
          '4 ) Borrow book\n',
          '5 ) To Return book\n',
          '6 ) Quit')

#Sub Members menu
def sub_Menu():
    '''Views menu to sort by categories'''
    print('0 ) View by Author\n'
          '1 ) View by Genre\n'
          '2 ) View by Year of release\n',
          '3 ) View by Publisher\n',
          '4 ) Back\n',
          'Choose option')
        
def user_make():
    '''Creates a user'''
    print("Write your preferred ID")
    iD = input()
    
    print("ENTER A STRONG PASSWORD")
    pwd = input()
    new_user(iD,pwd)


#Library functions
def show_all_books(option = None):
    '''Shows all books'''
    for idx , bookEntry in enumerate(inventory_dict):
        print(idx , bookEntry['Title'])
    print()

def show_all_users():
    '''Shows all users to librarian'''
    for idx , userEntry in enumerate(user_dict):
        print(idx , userEntry['User'])
    print()

def input_book():
    '''Inputs a book by librarian'''
    bookName = input("Enter book name - ")
    author = input("Enter the author - ")
    genre = input("Enter genre - ")
    year = input("Enter year of publishing - ")
    publisher = input("Enter publisher - ")

    book_Entry(bookName , author , genre , year , publisher)
    print()

def busy_books():
    '''Shows books and users to librarian'''
    for idx , userEntry in enumerate(user_dict):
        if userEntry['Current'] != []:
            print(idx , userEntry['User'],userEntry['Current'])
    print()

def quit_(option = None):
    pass

def option_Func(choice):
    '''Librarian function'''
    Lib_func = {0: show_all_books, 1 : show_all_users ,
                2 : input_book , 3 : busy_books , 4 : quit_}
    return Lib_func

#User function   
def show_available_books(option):
    '''Shows only available books'''
    for idx,bookEntry in enumerate(inventory_dict):
        if bookEntry['Borrowed']== 'None':
           print(idx , bookEntry['Title'])
           print()
    
def show_cat_books(option):
    '''Shows books using categories'''
    choice_a = 0
    while choice_a != 4:
        sub_Menu()
        print()

        choice_a = int(input())

        if choice_a==4:
            break

        choices = ['Author','Genre','Year','Publisher']
        
        cat = choices[choice_a]
        subMenu = list(set([bookEntry[cat] for bookEntry in inventory_dict]))     
                        
        for ind,item in enumerate(subMenu):
            print(ind , item)
            print()

        choice_b = int(input("Enter choice "))
        theme = subMenu[choice_b]

        for idx,bookEntry in enumerate(inventory_dict):                
            if bookEntry[cat]== theme:
                print(idx , bookEntry['Title'])
                print()
                
def show_current(option):
    '''Shows books currently reading'''
    string = user_dict[option-1]['Current'].split(' ,')
    for bookNum in string:
        if bookNum == '':
            pass
        else:
            print(int(bookNum), inventory_dict[int(bookNum)]['Title'])

def borrow_books(option):
    '''Allows user to borrow book'''
    bookNum = int(input("BOOK NUMBER "))

    if inventory_dict[bookNum]['Borrowed']== 'None':
        print(inventory_dict[bookNum]['Title'])
        print()
        print(' 1 ) Confirm\n',
              ' 2 ) Back')
        dec = int(input('Enter choice '))

        if dec == 1:

            #CHANGING USER STATUS
            user_dict[option-1]['Current']+= f'{bookNum} ,'

            #CHANGING BOOK STATUS
            inventory_dict[bookNum]['Borrowed'] = option - 1

def return_book(option):
    '''Allows user to return books'''
    List = user_dict[option-1]['Current'].split(' ,')
    for bookNum in List:
        if bookNum == '':
            pass
        else:
            print(int(bookNum), inventory_dict[int(bookNum)]['Title'])

    Num = int(input("Enter book number "))
    List = user_dict[option-1]['Current'].split(' ,')
    for i in List:
        if i == f'{Num}' or i == f' {Num}':    
            List.remove(i)
    user_dict[option-1]['Current']= ''.join([i+' ,' for i in List])
    inventory_dict[Num]['Borrowed'] = 'None'

def option_Func_User(option):
    '''User Functions'''
    user_Func = { 0: show_all_books, 1: show_available_books ,
                  2: show_cat_books, 3: show_current ,
                  4: borrow_books, 5: return_book , 6: quit_}
    return user_Func

          
    
