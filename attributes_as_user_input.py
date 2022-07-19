class User():

    def __init__(self):
        """Constructor"""
        self.name = input("Enter your name: ")
        self.birthday = input("Enter your birthday: ")
        self.email  = input("Enter your email-address: ")
    
    def __str__(self):
        """Return Object values in string"""
        return f'User:\n{self.name}\n{self.birthday}\n{self.email}'

    def make_recommendation(self):
        """User can man an recommendation about an burger restaurant"""
        recommendation = input("Make a recommendation for a burger restaurant in London: ")
        print('The best burger restaurant in London is:', recommendation)

u1 = User()
print(u1)
u1.make_recommendation()