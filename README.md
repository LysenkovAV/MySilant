# Начало работы с электронной сервисной книжкой "Мой Силант"

## Доступные скрипты

В директории 'MySilant' нужно выполнить команду:

### `python manage.py runserver`

Для доступа к админ-панели необходимо перейти по ссылке [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

Для начала работы с сервисной книжной необходимо перейти по ссылке [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Краткое описание функционала

- регистрация для пользователей закрыта
- администратор создает пользователей и наделяет их правами одной из групп (клиенты, сервисные компании, менеджеры)
- клиенты, сервисные компании и менеджеры могут авторизовываться с помощью логина и пароля, которые получены от администратора, и работать с базой данных с соответствующими ограничениями
- для редактирования справочников менеджеры должны получить от администратора статус персонала для доступа в админ-панель
- неавторизованным пользователям доступны только ограниченные данные о технике
- клиентам доступны для работы данные только о той технике, которая ими эксплуатируется
- сервисным компаниям доступны для работы данные только о той технике, которая ими обслуживается
- менеджерам доступны для работы данные о всей технике
- изменение существующих данных о машине доступно (менеджерам) при клике на ссылку с номером машины в таблице
- изменение существующих данных о техническом обслуживании доступно (всем пользователям) при клике на дату проведения ТО в таблице
- изменение существующих данных о рекламации доступно (менеджерам и сервисным организациям) при клике на дату отказа в таблице