from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def home(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def omlet(request):
    person = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Омлет',
        'recipe': {
            'яйца, шт': 2 * person,
            'молоко, л': round(0.1 * person, 1),
            'соль, ч.л.': round(0.5 * person, 1),
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    person = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Паста',
        'recipe': {
            'макароны, г': round(0.3 * person, 1),
            'сыр, г': round(0.05 * person, 2),
        }
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    person = int(request.GET.get('servings', 1))
    context = {
        'dish': 'Бутерброд',
        'recipe': {
            'хлеб, ломтик': 1 * person,
            'колбаса, ломтик': 1 * person,
            'сыр, ломтик': 1 * person,
            'помидор, ломтик': 1 * person,
        }
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
