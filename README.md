# qa_python

test_add_new_book_invalid_length
Тест: книга не добавляется, если имя пустое или превышает 40 символов

test_new_book_has_no_genre_by_default
Тест: у новой книги жанр по умолчанию отсутствует (пустая строка)

test_set_book_genre_sets_valid_genre
Тест: установка корректного жанра работает корректно

test_set_book_genre_ignores_invalid_genre
Тест: установка некорректного жанра игнорируется

test_get_books_with_specific_genre
Тест: получаем список книг определённого жанра

test_get_books_genre_returns_all_books
Тест: получаем весь словарь книг и проверяем, что он содержит добавленные книги

test_get_books_for_children_excludes_age_rated
Тест: книги с возрастным рейтингом не включаются в список детских книг

test_add_book_in_favorites_adds_once
Тест: добавление книги в избранное работает, и дубликаты не добавляются

test_add_book_in_favorites_does_nothing_if_not_exists
Тест: попытка добавить несуществующую книгу в избранное — игнорируется

test_delete_book_from_favorites_removes_book
Тест: удаление книги из избранного работает корректно

test_get_list_of_favorites_books_returns_correct_list
Тест: получаем правильный список избранных книг


test_get_book_genre_returns_correct_genre
Тест: метод возвращает корректный жанр, если он установлен