import csv,os
from pathlib import Path
def read_csv(path):
    data_folder=Path("/Tests/Data/")
    test_add_file_path1 = data_folder / path
    test_add_file_path=test_add_file_path1.absolute()
    csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
    next(csv_reader)
    test_row_list = list()
    for row in csv_reader:
        test_row_list.append(row)
    return test_row_list