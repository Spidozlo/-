class Publication:
    def __init__(self, title):
        self.title = title

    def info(self):
        return f'Название: {self.title}'


class Book(Publication):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def info(self):
        return f'Book: {self.title}, {self.author}'


class Magazine(Publication):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def info(self):
        return f'magazine: {self.title}, №{self.issue_number}'


class Library:
    def __init__(self, name):
        self.name = name
        self.list_of_books = []

    def add_new_book_or_magazine(self, new_book_or_magazine: Publication):
        self.list_of_books.append(new_book_or_magazine)

    def __str__(self):
        result = []
        if self.list_of_books:
            for obj in self.list_of_books:
                result.append(obj.info())
            return "\n".join(result)
        else:
            return "Пустая библиотека"


class Student:
    def __init__(self, name):
        self.name = name

    def take_book_from_library(self, obj_library: Library, obj_publication: Publication):
        if obj_publication in obj_library.list_of_books:
            obj_library.list_of_books.remove(obj_publication)
            print(f'Студент {self.name} взял {obj_publication.title} из {obj_library.name}')
        else:
            print(f'Публикация {obj_publication.title} отсутствует в {obj_library.name}')


class University:
    def __init__(self, name):
        self.list_student = []
        self.name = name

    def add_student(self, student):
        self.list_student.append(student)
        print(f'Студент по имени {student.name} принят в БГУФК')

    def full_list_of_students(self):
        counter = 1
        if self.list_student:
            print("Полный список студентов БГУФК:")
            for student in self.list_student:
                print(f'{counter}) {student.name}')
                counter += 1
        else:
            print("Пока что студентов нет")


oleg = Student('Олег')
a = University("БГУФК")

University.full_list_of_students(a)
a.add_student(oleg)
oleg2 = Student('флег')
oleg3 = Student('зямллег')
oleg4 = Student('ваделег')
a.add_student(oleg2)
a.add_student(oleg3)
a.add_student(oleg4)
a.full_list_of_students()

library = Library('1 Library of Pushkin')

book = Book('Yznik Azkabana', 'Joan Rouling')
magazine = Magazine('Lohoped', 22)
post1 = Publication('Solomon')
library.add_new_book_or_magazine(book)
library.add_new_book_or_magazine(magazine)
library.add_new_book_or_magazine(post1)
print(library)

oleg.take_book_from_library(library, book)
oleg.take_book_from_library(library, magazine)

print(library)
