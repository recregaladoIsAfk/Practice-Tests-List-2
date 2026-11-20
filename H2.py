books = []
copies = []

for i in range(3):
    book = input("Title: ")
    books.append(book)
    num_copy = input("Copies: ")
    copies.append(num_copy)
    
target = input("Search Title: ")

def find(book, target):
    for i in range(len(books)):
        if books[i] == target:
            return (f"{target} has {copies[i]} copies")
        return "Not in the library"
print(find(books, target))