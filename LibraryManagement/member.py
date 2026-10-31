class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def borrow_limit(self):
        return 2

    def loan_period(self):
        return 14

    def calculate_fine(self, overdue_days):
        return overdue_days * 10


class StudentMember(Member):

    def borrow_limit(self):
        return 3

    def loan_period(self):
        return 14

    def calculate_fine(self, overdue_days):
        return overdue_days * 10


class TeacherMember(Member):

    def borrow_limit(self):
        return 5

    def loan_period(self):
        return 30

    def calculate_fine(self, overdue_days):
        return overdue_days * 5