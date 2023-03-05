from django.shortcuts import redirect
from django.shortcuts import render
from users.models import CustomUser


def home_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    return render(request, 'home.html', {'points': points, 'badge': badge})


def history1_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')
        q5 = request.POST.getlist('question5')
        p = 0
        if q1 == ['Земли, лежащие на юг от границы государства до берегов Крыма.']:
            p += 10
        if q2 == ['1586г.']:
            p += 13
        if q3 == ['Участки незаселенной еще территории, которые сдавались в аренду для рыбной ловли, добычи пушных '
                  'зверей, сбора меда диких пчел.']:
            p += 19
        if q4 == ['В Москву.']:
            p += 18
        if q5 == ['Из «Сторожевой книги».']:
            p += 15

        done = CustomUser.objects.get(id=nam)
        if not done.test_1:
            done.points += p
            done.test_1 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history1.html', {'points': points, 'badge': badge})


def history2_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')
        q5 = request.POST.getlist('question5')
        p = 0
        if q1 == ['После поражения в первом Азовском походе.']:
            p += 14
        if q2 == ['Здание для хранения военного имущества.']:
            p += 15
        if q3 == ['Визит известного мореплавателя Витуса Беринга.']:
            p += 17
        if q4 == ['Нехватка рабочих рук.']:
            p += 11
        if q5 == ['10 января 1956 г.']:
            p += 19

        done = CustomUser.objects.get(id=nam)
        if not done.test_2:
            done.points += p
            done.test_2 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history2.html', {'points': points, 'badge': badge})


def history3_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')
        q5 = request.POST.getlist('question5')
        p = 0
        if q1 == ['Выгодное экономико-географическое положение.']:
            p += 14
        if q2 == ['C севера.']:
            p += 15
        if q3 == ['Азовская губерния - Воронежская губерния - потеря юго-западной части.']:
            p += 18
        if q4 == ['В 1773 году.']:
            p += 19
        if q5 == ['Перепланировать город.']:
            p += 18

        done = CustomUser.objects.get(id=nam)
        if not done.test_3:
            done.points += p
            done.test_3 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history3.html', {'points': points, 'badge': badge})


def history4_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')
        q5 = request.POST.getlist('question5')

        p = 0
        if q1 == ['«Историческое, географическое и экономическое описание Воронежской губернии».']:
            p += 10
        if q2 == ['В 1818 и 1820.']:
            p += 13
        if q3 == ['Детский парк «Орлёнок».']:
            p += 16
        if q4 == ['Орденом Святой Анны.']:
            p += 13
        if q5 == ['В 1891 году.']:
            p += 18

        done = CustomUser.objects.get(id=nam)
        if not done.test_4:
            done.points += p
            done.test_4 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history4.html', {'points': points, 'badge': badge})


def history5_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        p = 0
        if q1 == ['В 1912 году.']:
            p += 14
        if q2 == ['В Царском селе.']:
            p += 12
        if q3 == ['Черноземный Центр России нуждался в улучшениях сельскохозяйственного строя.']:
            p += 19

        done = CustomUser.objects.get(id=nam)
        if not done.test_5:
            done.points += p
            done.test_5 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history5.html', {'points': points, 'badge': badge})


def history6_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')
        q5 = request.POST.getlist('question5')

        p = 0
        if q1 == ['31 января 1918 г.']:
            p += 19
        if q2 == ['10 декабря 1917 г.']:
            p += 16
        if q3 == ['Г. К. Петров.']:
            p += 13
        if q4 == ['1 февраля.']:
            p += 14
        if q5 == ['В мае-июне 1929 г.']:
            p += 20

        done = CustomUser.objects.get(id=nam)
        if not done.test_6:
            done.points += p
            done.test_6 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history6.html', {'points': points, 'badge': badge})


def history7_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')
        q4 = request.POST.getlist('question4')

        p = 0
        if q1 == ['В районе Березовой рощи, стадиона «Динамо», улицы Ленина.']:
            p += 16
        if q2 == ['7 июля 1942 года.']:
            p += 13
        if q3 == ['Воронежско-Касторненской.']:
            p += 16
        if q4 == ['212 дней.']:
            p += 19

        done = CustomUser.objects.get(id=nam)
        if not done.test_7:
            done.points += p
            done.test_7 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history7.html', {'points': points, 'badge': badge})


def history8_page_view(request):
    nam = request.user.id
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if request.method == 'POST':
        q1 = request.POST.getlist('question1')
        q2 = request.POST.getlist('question2')
        q3 = request.POST.getlist('question3')

        p = 0
        if q1 == ['В 1990 году.']:
            p += 11
        if q2 == ['И. А. Бунину, С. А. Есенину, О. Э. Мандельштаму.']:
            p += 12
        if q3 == ['16.02.2008']:
            p += 17

        done = CustomUser.objects.get(id=nam)
        if not done.test_8:
            done.points += p
            done.test_8 = True
            done.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render(request, 'history8.html', {'points': points, 'badge': badge})


def articles_page_view(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0

    if CustomUser.objects.filter(id=nam).exists():
        art_2 = CustomUser.objects.get(id=nam).art_2
        art_3 = CustomUser.objects.get(id=nam).art_3
        art_4 = CustomUser.objects.get(id=nam).art_4
        art_5 = CustomUser.objects.get(id=nam).art_5
        art_6 = CustomUser.objects.get(id=nam).art_6

        if not art_2:
            key2 = 'Приобрести'
        else:
            key2 = 'Перейти'
        if not art_3:
            key3 = 'Приобрести'
        else:
            key3 = 'Перейти'
        if not art_4:
            key4 = 'Приобрести'
        else:
            key4 = 'Перейти'
        if not art_5:
            key5 = 'Приобрести'
        else:
            key5 = 'Перейти'
        if not art_6:
            key6 = 'Приобрести'
        else:
            key6 = 'Перейти'

    else:
        key2, key3, key4, key5, key6 = 'Приобрести', 'Приобрести', 'Приобрести', 'Приобрести', 'Приобрести'

    if 'confirm2' in request.POST:
        if CustomUser.objects.filter(id=nam).exists():
            us = CustomUser.objects.get(id=nam)
            if us.points >= 60:
                us.points -= 60
                us.art_2 = True
                us.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                                     'key5': key5, 'key6': key6, 'badge': badge})

    if 'confirm3' in request.POST:
        if CustomUser.objects.filter(id=nam).exists():
            us = CustomUser.objects.get(id=nam)
            if us.points >= 40:
                us.points -= 40
                us.art_3 = True
                us.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                                     'key5': key5, 'key6': key6, 'badge': badge})

    if 'confirm4' in request.POST:
        if CustomUser.objects.filter(id=nam).exists():
            us = CustomUser.objects.get(id=nam)
            if us.points >= 70:
                us.points -= 70
                us.art_4 = True
                us.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                                     'key5': key5, 'key6': key6, 'badge': badge})

    if 'confirm5' in request.POST:
        if CustomUser.objects.filter(id=nam).exists():
            us = CustomUser.objects.get(id=nam)
            if us.points >= 55:
                us.points -= 55
                us.art_5 = True
                us.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                                     'key5': key5, 'key6': key6, 'badge': badge})

    if 'confirm6' in request.POST:
        if CustomUser.objects.filter(id=nam).exists():
            us = CustomUser.objects.get(id=nam)
            if us.points >= 40:
                us.points -= 40
                us.art_6 = True
                us.save()
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                                     'key5': key5, 'key6': key6, 'badge': badge})

    return render(request, 'articles.html', {'points': points, 'key2': key2, 'key3': key3, 'key4': key4,
                                             'key5': key5, 'key6': key6, 'badge': badge})


def articles_page_view1(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article1.html', {'points': points, 'badge': badge})


def articles_page_view2(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article2.html', {'points': points, 'badge': badge})


def articles_page_view3(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article3.html', {'points': points, 'badge': badge})


def articles_page_view4(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article4.html', {'points': points, 'badge': badge})


def articles_page_view5(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article5.html', {'points': points, 'badge': badge})


def articles_page_view6(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article6.html', {'points': points, 'badge': badge})


def articles_page_view7(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'article7.html', {'points': points, 'badge': badge})


def quizzes_page_view(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'quizzes.html', {'points': points, 'badge': badge})


def account_page_view(request):
    nam = request.user.id
    badge = 'Крепостной крестьянин'
    if CustomUser.objects.filter(id=nam).exists():
        pq = CustomUser.objects.get(id=nam).points
        if int(pq) < 50:
            badge = 'Высокопочтенный крепостной крестьянин'
        elif int(pq) < 200:
            badge = 'Высокопочтенный мещанин'
        elif int(pq) < 400:
            badge = 'Высокопочтенный купец'
        else:
            badge = 'Высокопочтенный cтолбовой дворянин'
    if CustomUser.objects.filter(id=nam).exists():
        points = CustomUser.objects.get(id=nam).points
    else:
        points = 0
    return render(request, 'account.html', {'points': points, 'badge': badge})
