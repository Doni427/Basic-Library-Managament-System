class Library:
   
    #  __init__ function with an argument fileName. It will open the file in 'a+' mode to read and append to the file.
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.booksObj = open(fileName, "a+")
# listBooks() method will list the book objects in our file by seperating them with comma and print it to console.

    def listBooks(self):
        self.booksObj.seek(0)
        for line in self.booksObj:
            bookInfo = line.strip().split(',')
            bookName, author, releaseDate, numberOfPages = bookInfo
            print("Book Name:", bookName, "Author:", author, "Release Date:",
                  releaseDate, "Number of Pages:", numberOfPages)
            print("----------------------------------------------------------------------------------------------\n")

# =============================================================================
#  addBook() function will take 4 input from the user to add book. After user gives inputs.
# The function will append inputs to the file by f string and seperate them with commas for clarification.
#
# =============================================================================

    def addBook(self):
        bookName = input("Enter book title: ")
        author = input("Enter author name: ")
        releaseDate = input("Enter release date: ")
        numberOfPages = input("Enter number of pages: ")
        bookInfo = f"{bookName},{author},{releaseDate},{numberOfPages}\n"
        self.booksObj.write(bookInfo)
        print(bookName+" book added to the system successfully.\n")

# =============================================================================
# removeBook function will delete a book from the file. At first, seek() function is used to go to the first entry of our file.
# After that,file is read by the readlines(). Locates the wanted index and remove it. After removal we print non-deleted 
# values to file.
# =============================================================================

    def removeBook(self):
        bookToDelete = input("Enter the title of the book to delete: ")
        self.booksObj.seek(0)
        books = self.booksObj.readlines()
        self.booksObj.seek(0)
        self.booksObj.truncate()
        for book in books:
            if not book.startswith(bookToDelete):
                self.booksObj.write(book)
        print(bookToDelete + " book deleted from the system.\n")

# __del__ function is destructor to close the file.

    def __del__(self):
        self.booksObj.close()


# Library instance is created by the constructor function.

lib = Library("books.txt")

# =============================================================================
# While loop is used to create a menu for the application. 4 input is expected from the user. (1,2,3) for functions we defined above.
# 'q' input is for quit. If user wants to enter something different than wanted inputs, base case will print "Invalid operation!!"
# =============================================================================

while True:
    print("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Press q to quit")

    operation = input("Please select your operation: \n")

    if operation == '1':
        lib.listBooks()
    elif operation == '2':
        lib.addBook()
    elif operation == '3':
        lib.removeBook()
    elif operation == 'q':
        print("Exiting the program...")
        break
    else:
        print("Invalid operation!!!\n")
