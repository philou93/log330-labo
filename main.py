# -*- coding: utf-8 -*-
"""
Nom module: main
Auteur: Philippe Audet-Fortin
Date 15 juin 2018
Description: Main des tp.
"""
from my_math_module import my_math_module as mmm
from Reader import MyReader as mr


def tp1():
    """ Fonction pour le tp1 """
    numbers = mr.read_csv_data("test_tp1.csv")
    mean = mmm.mean(numbers)
    variance = mmm.variance(numbers, mean)
    std_der = mmm.std_derivation(variance)
    print("moyenne: {:10.2f}".format(mean))
    print("variance: \t{:10.2f}".format(variance))
    print("ecart-type: {:7.2f}".format(std_der))


def tp2():
    """ Fonction pour le tp2 """
    numbers = mr.read_csv_data("test_tp2.csv")
    corelation = mmm.caculate_correlation(numbers)
    print("corrélation: {:0.6f}".format(corelation))
    print(mmm.interprete_correlation_in_word(corelation))


def tp3():
    """ Fonction pour le tp3 """
    def _ask_for_x_value(slope, const):
        """ Demande une valeur x pour retourner une valeur y """
        x_val = float(mr.get_user_input("Entrez une valeur de x: "))
        y_val = slope*x_val + const
        return y_val

    def _ask_for_y_value(slope, const):
        """ Demande une valeur y pour retourner une valeur x """
        y_val = float(mr.get_user_input("Entrez une valeur de y: "))
        x_val = (y_val - const)/slope
        return x_val

    numbers = mr.read_csv_data("test_tp3.csv")
    slope = mmm.calculate_slope(numbers)
    const = mmm.calculate_const(numbers, slope)
    print("slope: {:8.6f}".format(slope))
    print("const: {:8.6f}".format(const))
    print(_ask_for_x_value(slope, const))
    print(_ask_for_y_value(slope, const))


def tp4():
    """ Fonction pour le tp4 """
    data = mr.read_csv_data("test_tp4.csv", 2, 1)
    numbers = mr.interpret_data_for_hours_and_result(data,6)
    corelation = mmm.caculate_correlation(numbers)
    print("corrélation: {:0.6f}".format(corelation))
    desc = mmm.interprete_correlation_in_word(corelation)
    print(desc)

def  tp5():
    """ Fonction pour le tp5 """
    numbers = mr.read_csv_data("test_tp5.csv")
    xk = float(mr.get_user_input("Quelle valeur voulez-vous chercher l'intervalle de confiance?"))
    slope = mmm.calculate_slope(numbers)
    const = mmm.calculate_const(numbers, slope)
    variance = mmm.variance_with_regression(numbers, slope, const)
    std_dev = mmm.std_derivation(variance)
    student_val = mmm.get_student()
    interval = mmm.calculate_interval(xk, numbers, std_dev, student_val)
    yk = const + xk*slope
    bounds = mmm.get_bounds_interval(interval, yk)
    print("Intevalle = {:0.6f}".format(interval))
    print("Limite supérieure = {:0.6f}".format(bounds[0]))
    print("Limite inférieure = {:0.6f}".format(bounds[1]))

#tp1()
#tp2()
#tp3()
#tp4()
tp5()