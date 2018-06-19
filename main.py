# -*- coding: utf-8 -*-
"""
Nom module: main
Auteur: Philippe Audet-Fortin
Date 15 juin 2018
Description: Main des tp.
"""
from my_math_module import my_math_module as mmm
from Reader import MyReader as mr


# Partie pour le TP1
# numbers = mr.read_csv_data_to_float("test_tp1.csv")
# mean = mmm.mean(numbers)
# variance = mmm.variance(numbers, mean)
# std_der = mmm.std_derivation(variance)
# print("moyenne: {:10.2f}".format(mean))
# print("variance: \t{:10.2f}".format(variance))
# print("ecart-type: {:7.2f}".format(std_der))

# Partie pour le TP2
numbers = mr.read_csv_data("test_tp2.csv")
corelation = mmm.caculate_corelation(numbers)
print("corrélation: {:0.6f}".format(corelation))
print(mmm.interprete_corelation_in_word(corelation))


# Partie pour le TP3
def ask_for_x_value(slope, const):
    """ Demande une valeur x pour retourner une valeur y """
    x_val = float(mr.get_user_input("Entrez une valeur de x: "))
    y_val = slope*x_val + const
    return y_val


def ask_for_y_value(slope, const):
    """ Demande une valeur y pour retourner une valeur x """
    y_val = float(mr.get_user_input("Entrez une valeur de y: "))
    x_val = (y_val - const)/slope
    return x_val


numbers = mr.read_csv_data("test_tp3.csv")
print(numbers)
slope = mmm.calculate_slope(numbers)
const = mmm.calculate_const(numbers, slope)
print("slope: {:8.6f}".format(slope))
print("const: {:8.6f}".format(const))
print(ask_for_x_value(slope, const))
print(ask_for_y_value(slope, const))

