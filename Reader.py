import csv


class MyReader:

    @staticmethod
    def read_csv_data(file):
        numbers = []
        header_readed = False
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if not header_readed:
                    header_readed = True
                    continue
                if len(row) > 1:
                    numbers.append([float(e.replace(',', '.')) for e in row])
                else:
                    numbers.append(float(row.replace(',', '.')))
        return numbers

    @staticmethod
    def get_user_input(msg):
        value = input(msg)
        return value
