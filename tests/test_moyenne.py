import pytest
from MyMathModule import MyMathModule as mmm


numbers = []
def before_test():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

# Les fonctions de test doit debuter par test_
# On verifie si une erreur est lancé si la liste des nombres est vide et on divise par 0
def test_CT7():
    before_test()
    assert mmm.mean(numbers) > 638


def test_CT8():
    before_test()
    assert mmm.mean(numbers) < 639



def test_CT8():
    before_test()
    assert mmm.mean(numbers) != 5656
