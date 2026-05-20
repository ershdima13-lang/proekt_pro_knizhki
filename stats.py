from models import Book

class Stats():
    def __init__(self, data: list[Book]):
        self.data = data

    def view_authors_stats(self):
        print("Статистика по авторам:\n")
        ratings = {}
        for i in self.data:
            if ratings.get(i.author) == None: ratings[i.author] = []
            ratings[i.author].append({"name":i.name, "rating":i.rating})

        for k, v in ratings.items():
            author_ratings = []
            author_books = []
            for i in ratings[k]:
                author_ratings.append(i["rating"])
                author_books.append(i["name"])
            avg = sum(author_ratings) / len(author_ratings)
            print(f"{k}:\n\tСредняя оценка: {avg}\n\tКниги: {author_books}")

    def view_avg(self):
        print(f"Всего книг прочитано: {len(self.data)}")
        for i in self.data:
            print(f"* Название: {i.name}, автор: {i.author}, оценка: {i.rating}, дата прочтения: {i.date}")