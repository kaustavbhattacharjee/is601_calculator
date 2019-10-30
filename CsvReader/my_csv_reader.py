import csv,os
from pathlib import Path
def read_csv(path):
    data_folder="Tests/Data/"+path
    #test_add_file_path1 = data_folder / path
    test_add_file_path1_x = Path(data_folder)
    test_add_file_path=test_add_file_path1_x.absolute()
    csv_reader = csv.reader(open(test_add_file_path, 'r'), delimiter=',')
    next(csv_reader)
    test_row_list = list()
    for row in csv_reader:
        test_row_list.append(row)
    return test_row_list