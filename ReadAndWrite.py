def read_Lib(FILE):

    with open(FILE,'r') as file:
        header = file.readlines(1)
        List = ''.join(header).strip('\n').split(', ')
        A = []
        for line in file.readlines():
            strval = line.strip('\n').split(', ')
            A.append({List[1] : strval[1],
                      List[2] : strval[2],
                      List[3] : strval[3],
                      List[4] : strval[4],
                      List[5] : strval[5],
                      List[6] : strval[6]})
    return A

def read_User(FILE):

    with open(FILE,'r') as file:
        header = file.readlines(1)
        List = ''.join(header).strip('\n').split(', ')
        A = []
        for line in file.readlines():
            strval = line.strip('\n').split(', ')
            A.append({List[1] : strval[1],
                      List[2] : strval[2],
                      List[3] : strval[3]})
    return A

def write_Book(bookfile, inventory_dict):
    with open(bookfile,'w') as file:
        file.write('Sno, Title, Author, Genre, Year, Publisher, Borrowed\n')

        for idx, item in enumerate(inventory_dict):
            file.write(f"{idx}, "
                       f"{item['Title']}, "
                       f"{item['Author']}, "
                       f"{item['Genre']}, "
                       f"{item['Year']}, "
                       f"{item['Publisher']}, "
                       f"{item['Borrowed']}\n")

def write_User(userfile,user_dict):
    with open(userfile,'w') as file:

        file.write('Sno, User, Password, Current\n')

        for idx, user in enumerate(user_dict):
            file.write(f'{idx}, '
                       f'{user["User"]}, '
                       f'{user["Password"]}, '
                       f'{user["Current"]}\n')  
