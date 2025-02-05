Разработайте REST-сервис для управления виртуальными серверами (VPS) с использованием Django Rest Framework (DRF).

Объект VPS должен включать следующие параметры:

uid — уникальный идентификатор сервера.

cpu — количество процессорных ядер.

ram — объем оперативной памяти.

hdd — объем дискового пространства.

status — текущий статус сервера (например, started, blocked, stopped).

API должно предоставлять следующие возможности:

Создание нового виртуального сервера.

Получение данных о конкретном сервере по его uid.

Вывод списка всех серверов с поддержкой фильтрации по заданным параметрам.

Изменение статуса сервера (например, перевод в состояния started, blocked, stopped).