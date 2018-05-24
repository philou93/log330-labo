import pytest
from MyMathModule.MyMathModule import MyMathModule as mmm

# Les fonctions de test doit debuter par test_
def test_CT1():
    with pytest.raises(Exception) as e_info:
        mmm.mean([])
    assert True




