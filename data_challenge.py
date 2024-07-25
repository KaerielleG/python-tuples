#task 2
''' You are maintaining a library system where each book is stored as a tuple within a list. 
    Your task is to update this system by adding new books and ensuring no duplicates.
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
 '''

def add_books(library, new_books):
    library_set = set(library)
    added_books = []
    duplicate_books = []

    for book in new_books: 
        if book not in library_set: 
            library_set.add(book)
            added_books.append(book)
        else:
            duplicate_books.append(book)
    updated_library = list(library_set)
    return updated_library, added_books, duplicate_books

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_books = [("Fahrenheit 415", "Ray Bradbury"), ("1984", "George Orwell")]    

updated_library = added_books, duplicate_books = add_books(library, new_books)
print("Updated Library:", updated_library)
print("Added Books:", added_books)
print("Duplicate Books:", duplicate_books)
 
 