from models import Book

def print_stats(data: list[Book]):
    print("Отображение статистики...")
    print("-"*40)
    view_authors_stats(data)
    print("-"*40)

def view_authors_stats(data: list[Book]):
    print("Статистика по авторам:\n")
    ratings = {}
    for i in data:
        if ratings.get(i.author) == None: ratings[i.author] = []
        ratings[i.author].append(i.rating)

    for k, v in ratings.items():
        ratings[k] = sum(v) / len(v)
        print(f"{k}: {ratings[k]}")