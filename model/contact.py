class Contact:
    def __init__(self,
                 firstname=None, middlename=None, lastname=None,
                 address=None, title=None, company=None,
                 nickname=None, phone=None, email=None,
                 bday=None, bmonth=None, byear=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone = phone
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
