from book import Book
from member import StudentMember, TeacherMember
from library import Library


library = Library()


def main_menu():

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Register Member")
        print("7. Show Members")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Borrowing History")
        print("0. Exit")

        choice = input("\nEnter Your Choice: ")

        try:

            if choice == "1":

                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")

                book = Book(book_id, title, author)
                library.add_book(book)

            elif choice == "2":

                library.show_books()

            elif choice == "3":

                book_id = int(input("Enter Book ID: "))
                library.search_book(book_id)

            elif choice == "4":

                book_id = int(input("Enter Book ID: "))
                title = input("Enter New Title: ")
                author = input("Enter New Author: ")

                library.update_book(book_id, title, author)

            elif choice == "5":

                book_id = int(input("Enter Book ID: "))
                library.delete_book(book_id)

            elif choice == "6":

                member_id = int(input("Enter Member ID: "))
                name = input("Enter Member Name: ")

                print("1. Student")
                print("2. Teacher")

                member_type = input("Select Member Type: ")

                if member_type == "1":
                    member = StudentMember(member_id, name)

                elif member_type == "2":
                    member = TeacherMember(member_id, name)

                else:
                    print("Invalid Member Type!")
                    continue

                library.register_member(member)

            elif choice == "7":

                library.show_members()

            elif choice == "8":

                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Member ID: "))

                library.borrow_book(book_id, member_id)

            elif choice == "9":

                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Member ID: "))

                library.return_book(book_id, member_id)

            elif choice == "10":

                library.show_borrow_history()

            elif choice == "0":

                print("Thank you for using Library Management System!")
                break

            else:
                print("Invalid Choice! Try Again.")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main_menu()