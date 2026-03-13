from book import Book

b1 = Book(2407, "Learn Python ", "Affan")
b2 = Book(5783, "Mastering OOP ", "Budi")

print(b1.get_title() + b1.get_author())
print(b2.get_title() + b2.get_author())

b1.set_title("belajar python with doctor ")
b2.set_title("mastering OOP with mr ")

b1.set_author("affandes")
b2.set_author("budiman")

print(b1.get_title()+ b1.get_author())
print(b2.get_title()+ b2.get_author())
