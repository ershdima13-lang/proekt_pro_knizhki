from models import Book

def print_stats(data: list[Book]):
    print("Отображение статистики...")
    print("-"*40)
    view_authors_stats(data)
    print("-"*40)
    print(f"Всего книг прочитано: {len(data)}")

def view_authors_stats(data: list[Book]):
    print("Статистика по авторам:\n")
    ratings = {}
    for i in data:
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