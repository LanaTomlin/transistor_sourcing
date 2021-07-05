import csv
import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import os
import glob
#Enter desired filename here

def data_upload(data):
    if not (data == '=' or data == '+' or data == '.' or data == None or data == 'MAIN' or data == '.MODEL' or data == '.SUBCKT' or data == 'Q1' or data == ')' or data == '('):
        if(column !=None and type(column) != float):
            if(data.find('=')== True):

                parameter = data.split('=')
                for x in parameter:
                    clean_file.write(x)
                    clean_file.write(',')
            else:
                #if(data.find('+')):
                 #   data = data[-1:]
                clean_file.write(data)
                clean_file.write(',')

file_path = 'spice_models'
for file in os.listdir(file_path):
    print(file)
    filename = str(file)
    file_name = filename[:-4]
    clean_file = open(f"clean_data/{file_name}.csv", "w")

    try:
        with open(f"spice_models/{filename}") as csvfile:
            spice_model = pd.read_csv(csvfile, sep ="\s+", engine = 'python', comment = '*')

            spice_data= spice_model.values

            print(spice_model.index)
            print(spice_model.columns)
            print(spice_data[0])
            num_rows = len(spice_model)
            print(num_rows)
            for row in spice_data:
                for column in row:
                        if(type(column) == list):
                            for data in column:
                                data_upload(data)
                        else:
                            data_upload(column)
                    
    except ValueError:
        print("Bad file")






   
# for row in spice_model:
    # print(row)
    #print(row[0])
#while spice_model.read() != None:
#  if()
