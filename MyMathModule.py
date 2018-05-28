import csv
import math


class MyMathModule:

    @staticmethod
    def read_csv_data_to_float(file):
        numbers = []
        header_readed = False
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not header_readed:
                    header_readed = True
                    continue
                for elem in row:
                    numbers.append(float(elem))
        return numbers

    @staticmethod
    def std_derivation(variance):
        return math.sqrt(variance)

    @staticmethod
    def variance(numbers, mean):
        sum_distance = 0
        for elem in numbers:
            sum_distance += MyMathModule.distance(elem, mean)
        return sum_distance/(len(numbers)-1) # Si echantillon on fait n-1

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
