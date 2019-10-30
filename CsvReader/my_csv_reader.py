import csv
def read_csv(path):
    test_add_file_path = path
    csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
    next(csv_reader)
    test_row_list = list()
    for row in csv_reader:
        test_row_list.append(row)
    return test_row_list