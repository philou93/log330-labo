import pytest
from MyMathModule import MyMathModule as mmm


# Les fonctions de test doit debuter par test_
# On verifie si une erreur est lancé si la liste des nombres est vide et on divise par 0
def test_CT1():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    mean = mmm.mean(numbers)
    assert mmm.variance(numbers,mean) > 391417

def test_CT2():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    mean = mmm.mean(numbers)
    assert mmm.variance(numbers,mean) < 391418

def test_CT3():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    mean = mmm.mean(numbers)
    assert mmm.variance(numbers,mean) != 5656
