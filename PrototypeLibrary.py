import copy


class BookPrototype:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def clone(self):
        return copy.deepcopy(self)


class Library:
    def __init__(self):
        self.prototype_fiction = BookPrototype("Гаррі Піт", "Джон Ролінг", "Привід")
        self.prototype_non_fiction = BookPrototype("Гаррі Поттер", "Джоан роулінг", "Пригоди")

    def create_fiction_book(self):
        return self.prototype_fiction.clone()

    def create_non_fiction_book(self):
        return self.prototype_non_fiction.clone()


library = Library()

fiction_book_1 = library.create_fiction_book()
fiction_book_2 = library.create_fiction_book()

non_fiction_book_1 = library.create_non_fiction_book()
non_fiction_book_2 = library.create_non_fiction_book()

print(fiction_book_1.title, fiction_book_1.author, fiction_book_1.genre)
print(fiction_book_2.title, fiction_book_2.author, fiction_book_2.genre)

print(non_fiction_book_1.title, non_fiction_book_1.author, non_fiction_book_1.genre)
print(non_fiction_book_2.title, non_fiction_book_2.author, non_fiction_book_2.genre)
