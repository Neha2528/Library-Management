import os 
import my_functions
my_functions.print_options()
option = input()
books = []
while option !='X' and option !="x":
    if option == '1':
        books.append(my_functions.create_book())
    elif option == '2':
        my_functions.save_books(books)
    elif option == '3':
        books = my_functions.load_books()
    elif option == '4':
        print(my_functions.issue_book(books))
    elif option == '5':
        my_functions.return_book(books)
    elif option == '6':
        my_functions.update_book(books)
    elif option == '7':
        my_functions.show_all_books(books)
    elif option == '8':
        my_functions.show_book(books)
    else:
        print("The given command doesn't exists..")
    input("Press enter to continue.")
    os.system("cls")
    my_functions.print_options()
    option = input()
