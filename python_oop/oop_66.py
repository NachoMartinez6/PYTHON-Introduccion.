



## CREATING AND INVOKING METHODS


class Book:

    favorites = [""]
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


book1 = Book("Are you my mother?", 72)
book2 = Book("The Digging-est Dog", 72)

# Book.favorites.extend([book1, book2])

# print(Book.favorites)

# for b in Book.favorites:
#     print(b.title)

# print(book1)
# print(book2)

print(book1 == book2)

data = {book1, book2}

# data = ("Hello", "Hi")

print(hash(book1))