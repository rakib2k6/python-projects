from datetime import date, timedelta


class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_records = []

    # Add Book
    def add_book(self, book):

        for existing in self.books:
            if existing.book_id == book.book_id:
                print("Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")

    # Show Books
    def show_books(self):

        if not self.books:
            print("No books found!")
            return

        for book in self.books:
            book.show_details()
            print("-------------------")

    # Search Book
    def search_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                book.show_details()
                return book

        print("Book not found!")
        return None

    # Update Book
    def update_book(self, book_id, title, author):

        book = self.search_book(book_id)

        if book:
            book.title = title
            book.author = author
            print("Book updated successfully!")

    # Delete Book
    def delete_book(self, book_id):

        book = self.search_book(book_id)

        if book:
            if not book.is_available:
                print("Cannot delete a borrowed book!")
                return

            self.books.remove(book)
            print("Book deleted successfully!")

    # Register Member
    def register_member(self, member):

        for existing in self.members:
            if existing.member_id == member.member_id:
                print("Member ID already exists!")
                return

        self.members.append(member)
        print("Member registered successfully!")

    # Show Members
    def show_members(self):

        for member in self.members:
            print(
                f"ID: {member.member_id}, "
                f"Name: {member.name}, "
                f"Type: {type(member).__name__}"
            )

    # Find Member
    def find_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    # Borrow Book
    def borrow_book(self, book_id, member_id):

        book = self.search_book(book_id)
        member = self.find_member(member_id)

        if book is None or member is None:
            print("Invalid Book ID or Member ID!")
            return

        active_loans = sum(
            1 for record in self.borrow_records
            if record["member_id"] == member_id
            and record["return_date"] is None
        )

        if active_loans >= member.borrow_limit():
            print("Borrowing limit exceeded!")
            return

        if not book.borrow():
            print("Book is already borrowed!")
            return

        borrow_date = date.today()
        due_date = borrow_date + timedelta(days=member.loan_period())

        self.borrow_records.append({
            "book_id": book_id,
            "member_id": member_id,
            "borrow_date": borrow_date,
            "due_date": due_date,
            "return_date": None,
            "fine": 0
        })

        print("Book borrowed successfully!")
        print("Due Date:", due_date)

    # Return Book
    def return_book(self, book_id, member_id):

        book = self.search_book(book_id)
        member = self.find_member(member_id)

        if book is None or member is None:
            print("Invalid Book ID or Member ID!")
            return

        for record in self.borrow_records:

            if (
                record["book_id"] == book_id
                and record["member_id"] == member_id
                and record["return_date"] is None
            ):

                return_date = date.today()

                overdue_days = max(
                    0, (return_date - record["due_date"]).days
                )

                fine = member.calculate_fine(overdue_days)

                book.return_book()

                record["return_date"] = return_date
                record["fine"] = fine

                print("Book returned successfully!")
                print("Overdue Days:", overdue_days)
                print("Fine Amount:", fine, "Taka")

                return

        print("No active borrowing record found!")

    # Borrowing History
    def show_borrow_history(self):

        if not self.borrow_records:
            print("No borrowing history!")
            return

        for record in self.borrow_records:

            print("-------------------")
            print("Book ID:", record["book_id"])
            print("Member ID:", record["member_id"])
            print("Borrow Date:", record["borrow_date"])
            print("Due Date:", record["due_date"])
            print("Return Date:", record["return_date"])
            print("Fine:", record["fine"])