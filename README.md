#Тестовое задание:
В Django 2.2+ создать приложение с моделью Отзывы. Создать view для получения всех отзывов через GET и создания нового через POST. В админке добавить кнопку для этой модели, которая “публикует” отзыв, посылая запрос на сторонний сервер.

##Поля у модели должны быть следующие:
Автор (FK к пользователю, обязательное)
Рейтинг (не отрицательное, целое в границах 1-5)
Текст отзыва (текстовое поле, опциональное)
Дата создания (текущий таймстамп при создании записи)
Галочка опубликован или нет (обязательное, по умолчанию False)

##View:
Через POST запрос должен создаваться новый Отзыв в БД. Обязательные поля - рейтинг и автор. Функция должна быть доступна только авторизованным пользователям.
Через GET запрос должен отдаваться список всех отзывов со всеми полями модели. Функция должна быть доступна только всем пользователям.

##Админка:
Добавить отображение отзывов в админку. На странице объекта галочка Опубликован должна быть нередактируемой. Добавить отдельную кнопку “Опубликовать”, по нажатию на которую:
Галочка Опубликован устанавливается в True
Отправлять POST запрос по адресу https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4 с телом JSON {"author":USER_ID, "rating":RATING,”review”:REVIEW_TEXT}
