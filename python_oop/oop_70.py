class Book:

    def __init__(self, title, pages):
        print("-- Creating book --")
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        else:
            return False
    
    def __str__(self):
        return self.title + " is " + str(self.pages) + " pages long"
    
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        else:
            return False
    
    def __hash__ (self):
        return hash(self.title) ^ hash(self.pages) #mutable types


book_1 = Book("Are you my mother", 72)
book_2 = Book("Are you my mother", 72)

# print(book_1)
# print(book_2)

# print(book_1==book_2)
# print(hash(book_1) == hash(book_2))

print(id(book_1), id(book_2))
