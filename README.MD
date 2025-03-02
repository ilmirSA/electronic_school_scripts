# Управление оценками в электронном дневнике

Скрипт разработан для автоматизированного управления оценками и похвалами учеников в электронном дневнике, построенном на платформе Django. Он автоматически корректирует низкие оценки, удаляет дисциплинарные меры и генерирует похвалы для учеников.


### 1. Как запустить

1. **Клонировать репозиторий**:
   - Перейдите по [ссылке](https://github.com/devmanorg/e-diary.git) на репозиторий GitHub.
   - Клонирует репозиторий на свой сервер.

2. **Скопировать скрипт**:
   - Скопируйте файл со скриптом  `scripts.py` в директорию, где находится файл `manage.py`.

3. **Установить зависимости**:
   - Установите необходимые библиотеки.
     ```
     pip install -r requirements.txt
     ```

5. **Запустить скрипт**:
   - Откройте консоль и запустите Django shell с помощью команды:
     ```
     python manage.py shell
     ```
   - Импортируйте функции из `scripts.py` и выполните их:
     ```
     from scripts find_student, create_commendation, fix_marks, remove_chastisements
     
     # Получите ученика по имени
     
     student = find_student("Белозеров Авдей Федотович")
     
     # Исправьте оценки, удалите жалобы и создайте похвалу
     fix_marks(student)
     remove_chastisements(student)
     create_commendation(student,"Музыка")
     ```

