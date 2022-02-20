from django.shortcuts import render


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


def dish(request, dish):
    person = int(request.GET.get('servings', 1))
    recipe_new = {}
    if dish in DATA.keys():
        for ingredient, amount in DATA[dish].items():
            amount_new = amount * person
            recipe_new[ingredient] = amount_new
    else:
        dish = ''
    context = {
        'dish': dish.capitalize(),
        'recipe': recipe_new
    }
    return render(request, 'calculator/index.html', context)
