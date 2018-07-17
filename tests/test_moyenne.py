# -*- coding: utf-8 -*-

import pytest
from my_math_module import my_math_module as mmm


# Les fonctions de test doit debuter par test_
# On verifie si une erreur est lancé si la liste des nombres est vide et on divise par 0
def test_CT7():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    assert mmm.mean(numbers) > 638


def test_CT8():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    assert mmm.mean(numbers) < 639



def test_CT8():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    assert mmm.mean(numbers) != 5656
