import random

from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Schoolkid

COMPLIMENTS = [
    'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!',
    'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!',
    'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!',
    'Ты на верном пути!',
    'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',
]


def find_student(name):
    try:
        return Schoolkid.objects.get(full_name=name)
    except (
            Schoolkid.MultipleObjectsReturned,Schoolkid.DoesNotExist) as error:
        print(f"Произошла ошибка при поиске студента! {error}")


def create_commendation(child, lesson_name):
    lesson = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter).filter(
        subject__title=lesson_name).first()
    if lesson:
        compliment = random.choice(COMPLIMENTS)
        Commendation.objects.create(text=compliment, created=lesson.date, schoolkid=child, subject=lesson.subject,
                                    teacher=lesson.teacher)


def fix_marks(child):
    Mark.objects.filter(schoolkid=child, points__lte=3).update(points=5)


def remove_chastisements(child):
    zams = Chastisement.objects.filter(schoolkid=child)
    zams.delete()
