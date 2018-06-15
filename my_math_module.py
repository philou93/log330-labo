import math


class my_math_module:
    """ Module mathématique avec divers fonctions. """

    @staticmethod
    def std_derivation(variance):
        """ Retourne la racine carree d'une valeur. """
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers, mean):
        """ Retourne la variace par rapport à une liste de nombre et une
        moyenne passée en paramètre. """
        sum_distance = 0
        for elem in numbers:
            sum_distance += MyMathModule.distance(elem, mean)
        return sum_distance/(len(numbers)-1)
        # Si echantillon on fait n-1

    @staticmethod
    def pow(number, power):
        """ Retourne la valeur d'un nombre exposant un entier. """
        result = 1
        for i in range(0, power):
            result *= number
        return result

    @staticmethod
    def distance(number, mean):
        """ Retourne la différence au carré entre deux nombres. """
        dist = mean - number
        return MyMathModule.pow(dist, 2)

    @staticmethod
    def mean(numbers):
        """ Retourne la moyenne d'une liste de nombres passée en paramètre. """
        xsum = 0
        for n in numbers:
            xsum += n
        return xsum/len(numbers)

    @staticmethod
    def caculate_corelation(entry_list):
        """ Calcule la corrélation entre les valeurs d'une liste de paires. """
        number_of_row = len(entry_list)

        summation_xy = MyMathModule.summation_of_multiplication_of_list_elem(
            entry_list)
        summation_x = MyMathModule.summation_of_list_elem_at(entry_list, 0)
        summation_y = MyMathModule.summation_of_list_elem_at(entry_list, 1)

        numerator = number_of_row*summation_xy - summation_x*summation_y

        summation_x_to_sqr = MyMathModule.\
            summation_of_list_with_elem_at_to_square(entry_list, 0)
        summation_y_to_sqr = MyMathModule.\
            summation_of_list_with_elem_at_to_square(entry_list, 1)


        denominator_part_x = number_of_row*summation_x_to_sqr \
                             - MyMathModule.pow(summation_x, 2)
        denominator_part_y = number_of_row*summation_y_to_sqr \
                             - MyMathModule.pow(summation_y, 2)

        denominator = math.sqrt(denominator_part_x*denominator_part_y)

        return numerator / denominator

    @staticmethod
    def summation_of_multiplication_of_list_elem(list_xy):
        """ Fait la sommation des nultiplications d'une liste de paire passée
        en paramètre. """
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
        """ Fait la sommation d'un des deux nombre au carré dans la paire. """
        summation_to_square = 0
        for row in list_xy:
            summation_to_square += MyMathModule.pow(row[pos], 2)
        return summation_to_square

    @staticmethod
    def abs_value(value):
        """ Retourne la valeur absolue. """
        if value >= 0:
            return value
        else:
            return value * (-1)

    @staticmethod
    def interprete_corelation_in_word(corelation):
        """ Renvoit une intéprétation litéraire de la corrélation. """
        abs_cor = MyMathModule.abs_value(corelation)
        if abs_cor < 0.2:
            return "Nulle à faible"
        elif abs_cor < 0.4:
            return "Faible à moyenne"
        elif abs_cor < 0.7:
            return "Moyenne à forte"
        elif abs_cor < 0.9:
            return "Forte à très forte"
        else:
            return "Très forte à parfaite"

