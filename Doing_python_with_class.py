# Defining a new class Member.
class Member:
    """ Create a new member from uname and fname."""
    def__init__ (self, uname, fname):
        # Giving the object its attributes
        self.username = uname
        self.fullname = fname
# Creating a instance from a class
new_guy = Member('Rambo','Rocco Moe')

print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))
