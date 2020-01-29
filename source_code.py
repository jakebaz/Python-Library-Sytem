import random

class Books():
    #Initialize - create book details
    def __init__(self, title, author, year, copies, publisher, pub_date):
        try: #error handling to ensure the user enters the correct details and data types
            self.title = title
            self.author = author
            self.year = year
            self.copies = copies
            self.publisher = publisher
            self.pub_date = pub_date
            self.book_id = 0
            self.total_stock = 0
        except: #if fails user can call the method and again to retry
            print('Could not create book, please try again')

    #set/overwrite book details
    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_year(self, new_year):
        self.year = new_year

    def set_copies(self, new_copies):
        self.copies = new_copies

    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    def set_pub_date(self, new_pub_date):
        self.pub_date = new_pub_date

    #return book details
    def return_title(self):
        return self.title

    def return_author(self):
        return self.author

    def return_year(self):
        return self.year

    def return_copies(self):
        return self.copies

    def return_publisher(self):
        return self.publisher

    def return_pub_date(self):
        return self.pub_date

#=====================================================================================#

class BookList(Books): #Inherit from Books class
    def __init__(self): #Initialize
        self.library = {}
        self.total_stock = 0
    #store book created in Books()
    def store_book(self, bk):
        try:
            self.bk = bk
        except:
            print('Books instance not found')    
        self.bk.book_id = random.randint(1, 100000)
        self.library[self.bk.title.lower()] = {
        "Title": self.bk.title.lower(), #use of .lower() to ensure search results are found even when user enters an uppercase letter
        "Author": self.bk.author.lower(),
        "Year": self.bk.year,
        "Availability": self.bk.copies,
        "Publisher": self.bk.publisher.lower(),
        "Publication Date": self.bk.pub_date,
        "ID": self.bk.book_id}
        self.total_stock += self.bk.copies #add the number of copies to total stock so that returning the total number of books is accurate
        return self.library
            
    def search(self, keyword):
        try: #if user enters a number system won't crash
            for i in self.library: #find book in dictionary and print out to the user
                if keyword.lower() in self.library[i].values():
                    print(self.library[i])
                    break
                else:
                    print('No Books Found') #Error handling: if book not found, print 'No Books found'
                    break
        except:
            print('Please search for a Title, Author, Publisher or Publication Date')        
                    
    def delete_book(self, book_title):
        self.book_title = book_title
        try: #system won't crash if user enters a number or makes spelling mistake
            if self.book_title.lower() in self.library:
                c = self.library[self.book_title.lower()].get('Availability')
                self.total_stock -= c
                del self.library[book_title.lower()]
                print('This book has been successfully deleted')
            else:
                print('Book not found, please ensure you have typed correctly')     
        except:
            print('Book not found, please ensure you have typed correctly')   

    #return number of books in collection
    def num_of_books(self):
        print('There is currently', self.total_stock, 'books in your database')
        return self.total_stock
            
#=====================================================================================#

class Users():
    #Initialize - create user details
    def __init__(self, username, first_name, surname, house_num, street, postcode, email, dob):
        try: #error handling
            self.username = username
            self.first_name = first_name
            self.surname = surname
            self.house_num = house_num
            self.street = street
            self.postcode = postcode
            self.email = email
            self.dob = dob
        except: #if fails user can call the method and again to retry
            print('Could not create user, please try again')

    #return user details
    def return_username(self):
        return self.username

    def return_first_name(self):
        return self.first_name
    
    def return_surname(self):
        return self.surname

    def return_house_num(self):
        return self.house_num

    def return_street(self):
        return self.street

    def return_postcode(self):
        return self.postcode

    def return_email(self):
        return self.email
    
    def return_dob(self):
        return self.dob

    #change user details
    def change_username(self, new_un):
        self.username = new_un

    def change_first_name(self, new_fn):
        self.first_name = new_fn

    def change_surname(self, new_sn):
        self.surname = new_sn

    def change_house_num(self, new_hn):
        self.house_num = new_hn

    def change_street(self, new_street_name):
        self.street = new_street_name

    def change_postcode(self, new_pc):
        self.postcode = new_pc

    def change_email(self, new_email):
        self.email = new_email
        
    def change_dob(self, new_dob):
        self.dob = new_dob

#=====================================================================================#        
    
class UserList(Users): #Inherit from UserList class
    #Initialize
    def __init__(self):
        self.user_db = {}
    
    #Store users
    def store_user(self, user):
        try: #error handling for if the user is not in user_db
            self.user = user
        except:
            print('User not found')         
        if self.user.username in self.user_db: #no two users can have the same username
            print('Username already taken, please try again with a different username.')    
        else:       
            self.user_db[self.user.username.lower()] = { #use lower() on strings so that they match user inputs
            'First name': self.user.first_name.lower(),
            'Surname': self.user.surname.lower(),
            'House Number': self.user.house_num,
            'Street name': self.user.street.lower(),
            'Postcode': self.user.postcode.lower(),
            'Email address': self.user.email.lower(),
            'Date of birth': self.user.dob.lower()}
            return self.user_db
            
    #Remove a user    
    def remove_user(self, name): #add more than one user with the same name functionality
        self.name = name
        try:
            for i in self.user_db: #Loop through dictionary to find user
                if self.name.lower() in self.user_db[i].values(): #if user with given name is present, delete
                    del self.user_db[i]
                    print('This user has been successfully deleted')
                    break
                else:
                    print('There is no user with this name')
                    break  
        except:
            print(name, 'not found, please ensure you have typed correctly')           

    #Count total number of users    
    def count_users(self):
        count = len(self.user_db)
        print(count)
        return count           
                    
    #return a users details
    def return_user_details(self, un):
        u_details = []
        try:
            if un.lower() in self.user_db:
                print(self.user_db[un])
                u_details.append(self.user_db[un])
            else:
                print('User not Found')
        except: #catch error from .lower() if user enters a number 
            print('User not found') 
        return u_details    

#=====================================================================================#

class Loans(BookList, UserList): #Multiple Inheritence from BookList and UserList classes
    def __init__(self, bk_inst, user_inst): #Initialize
        self.bk_inst = bk_inst
        self.user_inst = user_inst
        self.user_loans = {}
        self.book_loan = []
        self.overdue_books = {}
        super().__init__()

    def borrow_book(self, book_title, username):
        try:
            if username.lower() not in self.user_inst.user_db: #error checking: if user name is 'user not found' is printed.
                print('User not found')               
                return
        except: #if an int is entered rather than a string print 'User not found'
            print('User not Found')
        try:    
            if book_title.lower() in self.bk_inst.library:
                c = self.bk_inst.library[book_title.lower()].get('Availability') 
                c -= 1
                self.bk_inst.library[book_title.lower()].update({'Availability': c}) #update library when book is taken out
                self.bk_inst.total_stock -= 1 #update total stock when book is taken out
                self.user_loans.setdefault(username.lower(), []).append(book_title.lower()) #append item to list in dictionary rather than replace it
                if c == 0:
                    del self.bk_inst.library[book_title.lower()]
                self.book_loan.append([username.lower(), book_title.lower()]) #for later use in function 'return_borrower_details'    
                print(username, 'is now borrowing', book_title)
        except:
            print('Book is not currently available')          

    def return_loan(self, book_title, username):
        try: #error check: if user spells incorrectly or enters number print 'User not found'
            if username.lower() not in self.user_inst.user_db: #error checking: if user name is 'user not found' is printed.
                print('User not found')               
                return
        except:
            print('User not found')
            return  
        try:        
            for i in self.user_loans.values():
                if book_title.lower() in i:
                    i.remove(book_title.lower()) #update user loans dictionary when book is returned
                    c = self.bk_inst.library[book_title.lower()].get('Availability')
                    c += 1
                    self.bk_inst.library[book_title.lower()].update({'Availability': c}) #update library when book is returned
                    self.bk_inst.total_stock += 1 #update total stock when book is returned
                    print(book_title, 'has been returned')
            if len(self.user_loans[username.lower()]) == 0:
                del self.user_loans[username.lower()] #if user returns their only book, they get removed from the loans dictionary
        except:
            print('Book could not be returned')

    def return_num_of_loans(self, username): #count and return the total number of books a user is borrowing
        try:
            if username.lower() in self.user_loans:
                l = len(self.user_loans[username.lower()])
                if l > 1:
                    print(username, 'is currently borrowing', l, 'books')
                elif l == 1:
                    print(username, 'is currently borrowing 1 book')            
            else:
                print(username, 'is not currently borrowing any books')
            return l
        except:
            print('Could not find specified user')           

    def return_overdue_books(self, book_title, username):
        try:
            if username.lower() not in self.user_inst.user_db: #error checking: if user name is 'user not found' is printed.
                print('User not found')               
                return
        except:
            print('Could not find user')        
        try:        
            for i in self.user_loans.values():
                if book_title.lower() in i:
                    i.remove(book_title.lower()) #update user loans dictionary when book is returned
                    c = self.bk_inst.library[book_title.lower()].get('Availability')
                    c += 1
                    self.bk_inst.library[book_title.lower()].update({'Availability': c}) #update library when book is returned
                    self.bk_inst.total_stock += 1 #update total stock when book is returned
                    print(book_title, 'has been returned')
            if len(self.user_loans[username.lower()]) == 0:
                print('There are currently no overdue books for this user.')
                del self.user_loans[username.lower()] #if user returns their only book, they get removed from the loans dictionary
        except:
            print('Book could not be returned')

    def return_borrower_details(self, book):
        try:
            for sublist in self.book_loan: #loop list to find if book is in the dictionary
                for element in sublist:
                    if element == book.lower():
                        sub = sublist #get sublist so that we can get the username of the user
                        usr = sub[0]
        except:
            print('Book not found')                  
        if usr in self.user_inst.user_db:
            print(self.user_inst.user_db[usr]) #print details of borrower of a given book
        details = []
        details.append(self.user_inst.return_first_name)
        details.append(self.user_inst.return_surname)
        details.append(self.user_inst.return_email)
        return details    #return first name, surname and email of borrower of a given book
        
#=====================================================================================#

def system_test():

    #instances of users
    user1 = Users('jk_baz16', 'Jake', 'Bazin', 17, 'Rosemary Avenue', 'NE14 4YA', 'jk.bazin@hotmail.co.uk', '16/05/1997')
    user2 = Users('elliewantcookie', 'Ellie', 'Victoria', 5, 'Grey St', 'NE12 2YN', 'ellie@gmail.com', '23/08/1995')
    user3 = Users('johnnyboy22', 'John', 'Witherham', 25, 'Hammersmith Lane', 'DH14BY', 'johnnyw22@yahoo.co.uk', '07/02/1987')
    user4 = Users('TigerBoy88', 'Mike', 'Tyson', 13, 'Beverly Hills', '96703', 'miketyson@hotmail.com', '30/06/1966')
    user5 = Users('jakeyboii', 'Jake', 'Manson', 12, 'Grey St', 'TY34 9UN', 'jakeymanson@googlemail.co.uk', '23/11/1993')

    #Store users created in Users class
    ul = UserList()
    ul.store_user(user1)
    ul.store_user(user2)
    ul.store_user(user3)
    ul.store_user(user4)
    ul.store_user(user5)
    
    #Create book instances
    bk1 = Books('The Two Towers', 'J J R Tolkien', 1954, 7, 'George Allen & Unwin', '11/11/1954')
    bk2 = Books('The Hunger Games', 'Suzanne Collins', 2008, 11, 'Scholastic Press', '14/09/2008')
    bk3 = Books('Harry Potter And The Order Of The Pheonix', 'J K Rowling', 2003, 2, 'Bloomsbury', '21/07/2003')
    bk4 = Books('The Da Vinci Code', 'Dan Brown', 2003, 5, 'Transworld and Bantom Books', '13/04/2003')
    bk5 = Books('Of Mice And Men', 'John Steinbeck', 1937, 1, 'Covici Friede', '1937')

    #Store Books previously created
    bl = BookList()
    bl.store_book(bk1)
    bl.store_book(bk2)
    bl.store_book(bk3)
    bl.store_book(bk4)
    bl.store_book(bk5)
    

    #Loan instance with atleast one loan
    loans = Loans(bl, ul)
    loans.borrow_book('The Hunger Games', 'jk_baz16')
    loans.borrow_book('Harry Potter And The Order Of The Pheonix', 'elliewantcookie')
    loans.borrow_book('The Two Towers', 'johnnyboy22')
    loans.borrow_book('The Da Vinci Code', 'jk_baz16')
    loans.return_loan('The Da Vinci Code', 'jk_baz16')

system_test() 