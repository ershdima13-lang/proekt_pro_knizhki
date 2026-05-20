from models import Book
import json
import os

class Storage():
    def __init__(self):
        self.data: list[Book] = self.load_data()

    def save_data(self, filename="saved_data.json"):
        with open(filename, "w", encoding="utf-8") as file:
            to_save = []
            for i in self.data: to_save.append({
                "author":i.author, 
                "name":i.name, 
                "rating":i.rating, 
                "date":i.date
            })
            json.dump(to_save, file, indent=4, ensure_ascii=False)

    def load_data(self, filename="saved_data.json") -> list[Book]:
        if not os.path.exists(filename):
            return []
        
        with open(filename, "r") as file:
            to_return: list[Book] = []
            file_contents = json.load(file)
            for i in file_contents:
                to_return.append(Book(
                    i["author"],
                    i["name"],
                    i["rating"],
                    i["date"]
                ))
        return to_return
    
    def delete_book_by_name(self):
        name = input("Введите название книги: ")
        for i in range(len(self.data)):
            if self.data[i] == name:
                self.data.pop(i)
                break
        print("В библиотеке нет книги с таким названием!")

    def add_book(self):
        name = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        if any(i.name == name and i.author == author for i in self.data):
            print("Книга с этим названием и автором уже была добавлена.")
            return
        date = input("Введите даты прочтения книги: ")
        rating = input("Введите оценку книги (1-5): ")
        while True:
            try:
                rating = (max(1, min(5, int(rating))))
                break
            except ValueError:
                print("Введите число!")
        self.data.append(Book(name, author, rating, date))