# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_shape = Shape(20, 25)
my_shape.print_size()
