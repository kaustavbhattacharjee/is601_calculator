import csv,os
from pathlib import Path
def read_csv(path):
    data_folder="Tests/Data/"+path
    relative_file_path = Path(data_folder)
    absolute_file_path=relative_file_path.absolute()
    f=open(absolute_file_path, 'r')
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    test_row_list = list()
    for row in csv_reader:
        test_row_list.append(row)
    f.close()
    return test_row_list