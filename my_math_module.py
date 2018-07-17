# -*- coding: utf-8 -*-
"""
Nom module: my_math_module
Auteur: Philippe Audet-Fortin
Date 15 juin 2018
Description: Amat de fonction mathematique.
"""
import math
from Reader import MyReader as mr


class my_math_module:
    """ Module mathematique avec divers fonctions. """

    def __init__(self):
        pass

    @staticmethod
    def std_derivation(variance):
        """ Retourne la racine carree d'une valeur. """
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers, mean):
        """ Retourne la variace par rapport a une liste de nombre et une
        moyenne passee en parametre. """
        sum_distance = 0
        for elem in numbers:
            sum_distance += my_math_module.distance(elem, mean)
        return sum_distance/(len(numbers)-1)
        # Si echantillon on fait n-1

    @staticmethod
    def pow(number, power):
        """ Retourne la valeur d'un nombre exposant un entier. """
        result = 1
        for _ in range(0, power):
            result *= number
        return result

    @staticmethod
    def distance(number, mean):
        """ Retourne la difference au carre entre deux nombres. """
        dist = mean - number
        return my_math_module.pow(dist, 2)

    @staticmethod
    def mean(numbers):
        """ Retourne la moyenne d'une liste de nombres passee en parametre. """
        xsum = 0
        for num in numbers:
            xsum += num
        return xsum/len(numbers)


    # Ajout TP2
    @staticmethod
    def caculate_correlation(entry_list):
        """ Calcule la correlation entre les valeurs d'une liste de paires. """
        number_of_row = len(entry_list)

        summation_xy = my_math_module.summation_of_multiplication_of_list_elem(
            entry_list)
        summation_x = my_math_module.summation_of_list_elem_at(entry_list, 0)
        summation_y = my_math_module.summation_of_list_elem_at(entry_list, 1)

        numerator = number_of_row*summation_xy - summation_x*summation_y

        summation_x_to_sqr = my_math_module.\
            summation_of_list_with_elem_at_to_square(entry_list, 0)
        summation_y_to_sqr = my_math_module.\
            summation_of_list_with_elem_at_to_square(entry_list, 1)


        denominator_part_x = number_of_row*summation_x_to_sqr \
                             - my_math_module.pow(summation_x, 2)
        denominator_part_y = number_of_row*summation_y_to_sqr \
                             - my_math_module.pow(summation_y, 2)

        denominator = math.sqrt(denominator_part_x*denominator_part_y)

        return numerator / denominator

    @staticmethod
    def summation_of_multiplication_of_list_elem(list_xy):
        """ Fait la sommation des nultiplications d'une liste de paire passee
        en parametre. """
        summation_xy = 0
        for row in list_xy:
            summation_xy += row[0] * row[1]
        return summation_xy

    @staticmethod
    def summation_of_list_elem_at(list_xy, pos):
        """ Fait la sommation d'un des deux nombre dans la paire. """
        summation = 0
        for row in list_xy:
            summation += row[pos]
        return summation

    @staticmethod
    def summation_of_list_with_elem_at_to_square(list_xy, pos):
        """ Fait la sommation d'un des deux nombre au carre dans la paire. """
        summation_to_square = 0
        for row in list_xy:
            summation_to_square += my_math_module.pow(row[pos], 2)
        return summation_to_square

    @staticmethod
    def abs_value(value):
        """ Retourne la valeur absolue. """
        if value >= 0:
            return value
        return value*(-1)

    @staticmethod
    def interprete_correlation_in_word(correlation):
        """ Renvoit une intepretation literaire de la correlation. """
        abs_cor = my_math_module.abs_value(correlation)
        if abs_cor < 0.2:
            return "Nulle a faible"
        elif abs_cor < 0.4:
            return "Faible a moyenne"
        elif abs_cor < 0.7:
            return "Moyenne a forte"
        elif abs_cor < 0.9:
            return "Forte a tres forte"
        return "Tres forte a parfaite"


    # Ajout TP3
    @staticmethod
    def calculate_slope(entry_list):
        """ Calcule la pente de la regression lineaire. """
        number_of_row = len(entry_list)

        summation_xy = \
            my_math_module.summation_of_multiplication_of_list_elem(entry_list)
        list_x = my_math_module.get_all_elem_in_list_at(entry_list, 0)
        list_y = my_math_module.get_all_elem_in_list_at(entry_list, 1)
        mean_x = my_math_module.mean(list_x)
        mean_y = my_math_module.mean(list_y)
        numerator = summation_xy - (number_of_row*mean_x*mean_y)

        summation_x_to_sqrt = \
            my_math_module.summation_of_list_with_elem_at_to_square(entry_list
                                                                    , 0)
        mean_x_to_sqrt = my_math_module.pow(mean_x, 2)
        denominator = summation_x_to_sqrt - (number_of_row*mean_x_to_sqrt)
        return numerator/denominator

    @staticmethod
    def calculate_const(entry_list, slope):
        """ Calcule la constante B0 d'une regression lineaire. """
        list_x = my_math_module.get_all_elem_in_list_at(entry_list, 0)
        list_y = my_math_module.get_all_elem_in_list_at(entry_list, 1)
        mean_x = my_math_module.mean(list_x)
        mean_y = my_math_module.mean(list_y)
        return mean_y - (slope*mean_x)

    @staticmethod
    def get_all_elem_in_list_at(list_xy, pos):
        """ Retourne les element a la position pos d'une liste d'element """
        new_list = []
        for ele in list_xy:
            new_list.append(ele[pos])
        return new_list

    #Ajout tp5
    @staticmethod
    def variance_with_regression(numbers, slope, const):
        """ Calculer la variance et utilise la distance entre la valeur y et
            la regression lineaire associee a cette valeur. """
        sum_distance = 0
        for elem_x, elem_y in numbers:
            y_reg = const + elem_x * slope
            dist = my_math_module.distance(elem_y, y_reg)
            sum_distance += dist
        return sum_distance / (len(numbers) - 1)

    @staticmethod
    def get_student():
        """ Fonction pour demander a l'usager le niveau de confiance qu'il souhaite
            pour student et qui retourne la valeur de student associee. """
        answ = mr.get_user_input("Choisissez la valeur du alpha desire: "
                                 "\n\tAppuyer \n\t\t 1 pour alpha = 0.7 "
                                 "\n\t\t 2 pour alpha = 0.9")
        if answ == "1":
            print("alpha = {:0.3f}".format(1.108))
            return 1.108
        elif answ == "2":
            print("alpha = {:0.3f}".format(1.860))
            return 1.860
        else:
            raise Exception("Mauvais choix.")

    @staticmethod
    def distance_with_mean(numbers, mean):
        """ Retourne la variace par rapport a une liste de nombre et une
        moyenne passee en parametre. """
        sum_distance = 0
        for elem in numbers:
            sum_distance += my_math_module.distance(elem, mean)
        return sum_distance

    @staticmethod
    def calculate_interval(x_k, numbers, std_dev, student_val):
        """ Fonction pour le calcule de l'intervalle """
        list_x = my_math_module.get_all_elem_in_list_at(numbers, 0)
        mean_x = my_math_module.mean(list_x)
        numerator = my_math_module.pow(x_k - mean_x, 2)
        denominator = my_math_module.distance_with_mean(list_x, mean_x)
        part_1 = student_val*std_dev
        part_2 = math.sqrt(numerator/denominator + 1 + 1/len(list_x))
        return part_1*part_2

    @staticmethod
    def get_bounds_interval(interval, y_k):
        """ Calcul les limite de l'intervalle. """
        return [y_k + interval, y_k - interval]
