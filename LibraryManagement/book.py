class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_available = True

    @property
    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True

        return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True

        return False

    def show_details(self):
        status = "Available" if self.__is_available else "Borrowed"

        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")