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
    def read_csv_data_for_tp4(file):
        numbers = []
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')[2:]
            for row in csv_reader:
                summation = 0
                for col in range(1, 6, 1):
                    summation += float(row[col].replace(',', '.'))
                numbers.append([float(row[7].replace(',', '.')), summation])
        return numbers

    @staticmethod
    def get_user_input(msg):
        value = input(msg)
        return value
