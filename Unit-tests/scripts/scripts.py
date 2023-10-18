from base_params import basic_rate, regions_dv, cook_book

def mortage_calc(region: str, num_child: int, is_sal: bool, is_ins: bool) -> int:
    if region.lower() in regions_dv:
        return 2
    else:
        if int(num_child) > 3:
            if is_sal:
                if is_ins:
                    discount = 3.5
                else:
                    discount = 1.5
            else:
                if is_ins:
                    discount = 3
                else:
                    discount = 1
        else:
            if is_sal:
                if is_ins:
                    discount = 2.5
                else:
                    discount = 0.5
            else:
                if is_ins:
                    discount = 1.5
                else:
                    discount = 0
    return basic_rate - discount

def zodiac(month: str, day: int) -> str:
    if month == 'январь':
        if day < 20:
            zodiac = 'Козерог'
        else:
            zodiac = 'Водолей'
    elif month == 'февраль':
        if day < 20:
            zodiac = 'Водолей'
        else:
            zodiac = 'Рыбы'
    elif month == 'март':
        if day < 21:
            zodiac = 'Рыбы'
        else:
            zodiac = 'Овен'
    elif month == 'апрель':
        if day < 20:
            zodiac = 'Овен'
        else:
            zodiac = 'Телец'
    elif month == 'май':
        if day < 21:
            zodiac = 'Телец'
        else:
            zodiac = 'Близнецы'
    elif month == 'июнь':
        if day < 21:
            zodiac = 'Близнецы'
        else:
            zodiac = 'Рак'
    elif month == 'июль':
        if day < 23:
            zodiac = 'Рак'
        else:
            zodiac = 'Лев'
    elif month == 'август':
        if day < 23:
            zodiac = 'Лев'
        else:
            zodiac = 'Дева'
    elif month == 'сентябрь':
        if day < 23:
            zodiac = 'Дева'
        else:
            zodiac = 'Весы'
    elif month == 'октябрь':
        if day < 24:
            zodiac = 'Весы'
        else:
            zodiac = 'Скорпион'
    elif month == 'ноябрь':
        if day < 23:
            zodiac = 'Скорпион'
        else:
            zodiac = 'Стрелец'
    elif month == 'декабрь':
        if day < 21:
            zodiac = 'Стрелец'
        else:
            zodiac = 'Козерог'
    return zodiac



person = 5

# first_count - это переменная, элементы списка первого уровня (блюда)
# second_count - это переменная, элементы списка второго уровня
def shop_list(person: int) -> str:
    text = ''
    for first_count in cook_book:
        text += '\n'
        for second_count in first_count:
            if isinstance(second_count, list):
                for ingredient in second_count:
                    quanty = int(ingredient[1])
                    ingredient[1] = ' ' + str(quanty * person)
                    text += ' ' + ','.join(ingredient).replace(',гр.', 'гр.').replace\
                        (',мл.','мл.') + '\n'
            else:
                text += second_count + ':' + '\n'
    return text

