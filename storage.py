from models import Book
import json
import os

class Storage():
    def __init__(self):
        self.data: list[Book] = self.load_data()

    def save_data(self, data: list[Book], filename="saved_data.json"):
        with open(filename, "w", encoding="utf-8") as file:
            to_save = []
            for i in data: to_save.append({
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
