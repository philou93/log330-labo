import pytest
from MyMathModule import MyMathModule as mmm


numbers = []
def before_test():
    numbers = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

# Les fonctions de test doit debuter par test_
# On verifie si une erreur est lancé si la liste des nombres est vide et on divise par 0
def test_CT4():
    before_test()
    mean = mmm.mean(numbers)
    var = mmm.variance(numbers,mean)
    assert mmm.std_derivation(var) > 625

def test_CT5():
    before_test()
    mean = mmm.mean(numbers)
    var = mmm.variance(numbers,mean)
    assert mmm.std_derivation(var) < 626

def test_CT6():
    before_test()
    mean = mmm.mean(numbers)
    var = mmm.variance(numbers,mean)
    assert mmm.std_derivation(var) != 625.1
