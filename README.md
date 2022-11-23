# MediaNation-test-task

### Habr scraper with RedisDb

## ТЗ

Скачать 10 000 страниц с сайта https://career.habr.com

Url-ы для скачивания лежат в csv файлике:
https://drive.google.com/file/d/1iHlRsw2QV-9asGpQDWEQ9kCp3UmoQs7n/view?usp=sharing

Запуск скрипта должен быть из командной строки.
Результаты парсинга положить на диск в отдельную папку.
Предусмотреть избежание блокировок со стороны сайта при массовом парсинге.

Требования:

1. Парсим без авторизации
2. Нужен код, рассчитанный на парсинг ±1 млн. страниц в день
3. Использовать параллельный подход к парсингу
4. Использовать ООП
5. Решить, что делать если парсинг прервется на середине и нужно будет заново перезапускать
6. Результаты парсинга каждого человека нужно сохранить в отдельный файлик в формате:
   первая строка - url человека, которого парсим
   вторая строка - имя и фамилию человека, которого парсим
   третья строка - сам html-код исходной страницы

При необходимости можем выделить прокси для тестов.

## Документация

### Запуск

1. Создайте и запустите Redis на порту 6379:16379 <br>
   - Пример создания в докере: <br>
     `docker pull redis` <br>
     `docker run --name some-redis -p 6379:16379 -d redis`
2. Запустите программу
   - Установите зависимости из <b>requirements.txt</b>
   - `python app/main.py`

## Описание

Приложение использует Redis для хранения индекса последнего выполненного url, чтобы при прерывание парсинга можно было перезапустить с точки остановки.
<br>
Ссылки которые не получилось спарсить храняться в <b>app/files/bad_urls/bad_urls.txt</b>. Они попадают туда с помощью Redis.
<br><br>
Для парсинга используется модуль <b>threading</b>, ссылки парсяться параллельно в 2 потока. Результат парсинга сохраняется в <b>app/files/results</b>.
