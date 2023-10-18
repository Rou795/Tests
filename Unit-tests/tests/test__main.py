from base_params import regions_dv, examples
from scripts.scripts import mortage_calc, zodiac, shop_list
from unittest import TestCase
import random as r
import pytest

# Класс для тестирования функции mortage_calc

class Mort_calc_test(TestCase):

# тестирование дисконта за регион

    def test_discount_region(self):
        test_num_child = [el for el in range(6)]
        expected = 2
        for region in regions_dv:
            for data in test_num_child:
                self.assertEqual(mortage_calc(region, data, r.choice((True, False)),
                                              r.choice((True, False))),
                                 expected)

# тестирование дисконта за кол-во детей

    def test_childrens_discount(self):
        test_num_child = [el for el in range(6)]
        expected_low = 7
        expected_high = 8
        for data in test_num_child:
            if data <= 3:
                self.assertEqual(mortage_calc('', data, False, False), expected_high)
            else:
                self.assertEqual(mortage_calc('', data, False, False), expected_low)

# тестирование дисконта за признак зарплатного клиента

    def test_sal_discount(self):
        test_num_child = 2
        is_ins = False
        expected_low = 7.5
        expected_high = 8
        for _ in range(50):
            is_sal = r.choice((True, False))
            if is_sal:
                self.assertEqual(mortage_calc('', test_num_child, is_sal, is_ins), expected_low)
            else:
                self.assertEqual(mortage_calc('', test_num_child, is_sal, is_ins), expected_high)

# тестирование дисконта за признак оформления страховки

    def test_ins_discount(self):
        test_num_child = 2
        is_sal = False
        expected_low = 6.5
        expected_high = 8
        for _ in range(50):
            is_ins = r.choice((True, False))
            if is_ins:
                self.assertEqual(mortage_calc('', test_num_child, is_sal, is_ins), expected_low)
            else:
                self.assertEqual(mortage_calc('', test_num_child, is_sal, is_ins), expected_high)

# тестирование функции zodiac

@pytest.mark.parametrize(
    "month, day, expected",
    [
        ('апрель', 17, 'Овен'),
        ('октябрь', 24, 'Скорпион'),
        ('октябрь', 13, 'Весы'),
        ('январь', 1, 'Козерог')
    ]
)
def test_zodiac(month, day, expected):
    result = zodiac(month, day)
    assert result == expected

# тестирование функции shop_list с использованием
# параметризации

@pytest.mark.parametrize(
    "person, expected",
    [
        (1, examples[0]),
        (2, examples[1])
    ]
)
def test_shop_list(person, expected):
    result = shop_list(person)
    assert result == expected

