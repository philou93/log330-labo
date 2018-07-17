import csv


class MyReader:
    """ Fonctions pour lire les csv contenant les infos des tp. """

    def __init__(self):
        pass

    @staticmethod
    def read_csv_data(file, nb_lines_for_header=1, col_start=0):
        """ Lit les csv ordinaires. """
        numbers = []
        header_readed = 0
        with open(file, 'r', encoding='latin_1') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if header_readed < nb_lines_for_header:
                    header_readed += 1
                    continue
                row = row[col_start:]
                if len(row) > 1:
                    numbers.append([float(e.replace(',', '.')) for e in row])
                else:
                    numbers.append(float(row.replace(',', '.')))
            print(numbers)
        return numbers

    @staticmethod
    def interpret_data_for_hours_and_result(data, nb_x):
        """ Fait la sommation des heures d'étude pour chaque étudiant. """
        numbers = []
        for row in data:
            summation = 0
            for col in range(0, nb_x, 1):
                summation += row[col]
            numbers.append([row[nb_x], summation])
        return numbers

    @staticmethod
    def get_user_input(msg):
        """ Demande a l'usager une valeur. """
        value = input(msg)
        return value
