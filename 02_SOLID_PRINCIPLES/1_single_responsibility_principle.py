"""
> Single Responsibility Principle (SRP) is a principle of OOP that states
every class should have a single responsibility, and that responsibility 
should be entirely encapsulated by the class.

"""

# Example which does not follow SRP


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        # save user to database.
        pass

    def authenticate(self):
        # authenticate user against database.
        pass

    def send_email(self, to, subject, message):
        # send an email to specified recipient.
        pass


"""
In the above example, class has three responsibilities 
i.e., saving user info,authenticating user, shoot email for user.

Problems include:
1. Class becoming large and unwidely,which can make it difficult to understand and
   maintain.
2. Class being more prone to errors,as changes to the class to support one responsibility
   may unintentionally break code related to another responsiblity.
3. The overall design of the program becoming more complex, as it would require more
   coordination between the user class and other parts of the program.
4. The class being difficult to reuse in other parts of the program,due to it's
    diverse set of responsibilities.
"""

# Adressing above Problems with SRP:


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        # save user to database.
        pass


class Authenticate:
    def authenticate(self, user):
        # authenticate user against database.
        pass


class Emailer:
    def send_email(self, to, subject, message):
        # send an email to specified recipient.
        pass


""" 
In this revised design, each class has a single and unique responsibility and 
it can be judjed by it's Name.
"""
