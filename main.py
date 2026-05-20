from storage import Storage
from stats import Stats

class Main():
    def __init__(self):
        self.storage = Storage()
        self.stats = Stats(self.storage.data)

    def main(self):
        while True:
            command = input(
                "Введите команду:\n"
                "1. Добавить книгу\n"
                "2. Показать все книги\n"
                "3. Показать среднюю оценку\n"
                "4. Статистика по авторам\n"
                "5. Удалить книгу\n"
                "6. Выход\n"
            )

            if command == '1':
                self.storage.add_book()
            elif command == '2':
                self.stats.view_all()
            elif command == '3':
                self.stats.view_avg()
            elif command == '4':
                self.stats.view_authors_stats()
            elif command == '5':
                self.storage.delete_book_by_name()
            elif command == '6':
                self.storage.save_data()
                break
            else:
                print("Неизвестная команда. Введите число от 1 до 6.\n")

Main().main()