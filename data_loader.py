import csv
import os
import pandas as pd


def load_csv_as_list(file_path):
    print('COM731')
    print('COM731')
    if not os.path.exists(file_path):
        print('Error: File does not exist.')
        return None, None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            rows = list(csv.reader(file))
        header, data = rows[0], rows[1:]
        print('\nCSV loaded successfully using csv.reader().')
        print('Total records:', len(data))
        print('Total columns:', len(header))
        return header, data
    except Exception as error:
        print('Error while loading CSV:', error)
        return None, None


def load_csv_as_dataframe(file_path):
    if not os.path.exists(file_path):
        print('Error: File does not exist.')
        return None
    try:
        dataframe = pd.read_csv(file_path)
        print('\nCSV loaded successfully using pandas.read_csv().')
        print('DataFrame shape:', dataframe.shape)
        return dataframe
    except Exception as error:
        print('Error while creating DataFrame:', error)
        return None
