import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест: книга не добавляется, если имя пустое или превышает 40 символов
    @pytest.mark.parametrize("book_name", ["", "A"*41])
    def test_add_new_book_invalid_length(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        # Проверяем, что книга не добавлена
        assert book_name not in collector.get_books_genre()

    # Тест: у новой книги жанр по умолчанию отсутствует (пустая строка)
    def test_new_book_has_no_genre_by_default(self):
        collector = BooksCollector()

        collector.add_new_book("Новая книга")

        assert collector.get_book_genre("Новая книга") == ""

    # Тест: установка корректного жанра работает корректно
    def test_set_book_genre_sets_valid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")

        assert collector.get_book_genre("Дюна") == "Фантастика"

    # Тест: установка некорректного жанра игнорируется
    def test_set_book_genre_ignores_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Роман")  # жанра "Роман" нет в списке

        assert collector.get_book_genre("1984") == ""

    # Тест: получаем список книг определённого жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Шрек")
        collector.set_book_genre("Шрек", "Мультфильмы")

        collector.add_new_book("Крик")
        collector.set_book_genre("Крик", "Ужасы")

        result = collector.get_books_with_specific_genre("Мультфильмы")

        assert "Шрек" in result
        assert "Крик" not in result

    # Тест: получаем весь словарь книг и проверяем, что он содержит добавленные книги
    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()

        collector.add_new_book("Колобок")
        collector.add_new_book("Репка")

        books = collector.get_books_genre()

        assert "Колобок" in books and "Репка" in books

    # Тест: книги с возрастным рейтингом не включаются в список детских книг
    def test_get_books_for_children_excludes_age_rated(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")  # жанр с возрастным ограничением

        collector.add_new_book("Мадагаскар")
        collector.set_book_genre("Мадагаскар", "Мультфильмы")  # допустим для детей

        result = collector.get_books_for_children()

        assert "Оно" not in result
        assert "Мадагаскар" in result

    # Тест: добавление книги в избранное работает, и дубликаты не добавляются
    def test_add_book_in_favorites_adds_once(self):
        collector = BooksCollector()

        collector.add_new_book("Шрек")
        collector.add_book_in_favorites("Шрек")
        collector.add_book_in_favorites("Шрек")  # попытка повторного добавления

        favorites = collector.get_list_of_favorites_books()
        assert favorites.count("Шрек") == 1

    # Тест: попытка добавить несуществующую книгу в избранное — игнорируется
    def test_add_book_in_favorites_does_nothing_if_not_exists(self):
        collector = BooksCollector()

        collector.add_book_in_favorites("Несуществующая книга")

        assert collector.get_list_of_favorites_books() == []

    # Тест: удаление книги из избранного работает корректно
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

        collector.add_new_book("Матрица")
        collector.add_book_in_favorites("Матрица")
        collector.delete_book_from_favorites("Матрица")

        assert "Матрица" not in collector.get_list_of_favorites_books()

    # Тест: получаем правильный список избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()

        collector.add_new_book("Шрек")
        collector.add_new_book("Матрица")

        collector.add_book_in_favorites("Шрек")

        result = collector.get_list_of_favorites_books()

        assert result == ["Шрек"]