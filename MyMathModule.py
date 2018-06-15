import math


class MyMathModule:

    @staticmethod
    def std_derivation(variance):
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers, mean):
        sum_distance = 0
        for elem in numbers:
            sum_distance += MyMathModule.distance(elem, mean)
        return sum_distance/(len(numbers)-1)
        # Si echantillon on fait n-1

    @staticmethod
    def pow(number, power):
        result = 1
        for i in range(0, power):
            result *= number
        return result

    @staticmethod
    def distance(number, mean):
        dist = mean - number
        return MyMathModule.pow(dist, 2)

    @staticmethod
    def mean(numbers):
        xsum = 0
        for n in numbers:
            xsum += n
        return xsum/len(numbers)

    @staticmethod
    def caculateCorelation(entryList):
        number_of_row = len(entryList)

        summation_xy = MyMathModule.summationOfMultiplicationOfListElem(
            entryList)
        summation_x = MyMathModule.summationOfListElemAt(entryList, 0)
        summation_y = MyMathModule.summationOfListElemAt(entryList, 1)

        numerator = number_of_row*summation_xy - summation_x*summation_y

        summation_x_to_sqr = MyMathModule.summationOfListWithElemAtToSquare(
            entryList, 0)
        summation_y_to_sqr = MyMathModule.summationOfListWithElemAtToSquare(
            entryList, 1)


        denominator_part_x = number_of_row*summation_x_to_sqr \
                             - MyMathModule.pow(summation_x, 2)
        denominator_part_y = number_of_row*summation_y_to_sqr \
                             - MyMathModule.pow(summation_y, 2)

        denominator = math.sqrt(denominator_part_x*denominator_part_y)

        return numerator / denominator

    @staticmethod
    def summationOfMultiplicationOfListElem(list_xy):
        summation_xy = 0
        for row in list_xy:
            summation_xy += row[0] * row[1]
        return summation_xy

    @staticmethod
    def summationOfListElemAt(list_xy, pos):
        summation = 0
        for row in list_xy:
            summation += row[pos]
        return summation

    @staticmethod
    def summationOfListWithElemAtToSquare(list_xy, pos):
        summation_to_square = 0
        for row in list_xy:
            summation_to_square += MyMathModule.pow(row[pos], 2)
        return summation_to_square

    @staticmethod
    def absValue(value):
        if value >= 0:
            return value
        else:
            return value * (-1)

    @staticmethod
    def interpreteCorelationInWord(corelation):
        abs_cor = MyMathModule.absValue(corelation)
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


