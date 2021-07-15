import pandas as pd
import os
import component_sorting

#Enter desired component name here
#options: BJT
COMPONENT = "BJT"

def data_upload(data):
    if (data != None and data != float) :
        data.replace('+', ' ')

        if(data.find('=') != -1):
            parameter = data.split('=')
            for x in parameter:
                if(x != ''):
                    data_upload(x)
            data = ''
        if(data.find('+') != -1 ):
            data = data[1:]
        if(data.find('\n') != -1):
            data = data[:-1]
               
    if(data != '' and data != 'nan'):
        clean_file.write(str(data))
        clean_file.write(',')

file_path = f'{COMPONENT}/spice_models'
for file in os.listdir(file_path):
    filename = str(file)
    file_name = filename[:-4]
    clean_file = open(f"{COMPONENT}/clean_data/{file_name}.csv", "w")

    try:
        with open(f"{COMPONENT}/spice_models/{filename}") as rawfile:
            spice_model = []
            for line in rawfile:
                if(line.find('*') == -1):
                    remove_space = line.split(" ")
                    for data in remove_space:
                        if(data != '' and data != '\n' and data != '=' and data != '+' and data != '.' and data != None and data != 'MAIN' and data != '.MODEL' and data != '.SUBCKT' and data != 'Q1' and data != ')' and data != '('):
                            spice_model.append(data)
                  
            print(spice_model)
            for row in spice_model:
                    data_upload(row)
                    
    except ValueError:
        print("Bad file")

    clean_file.close()

if(COMPONENT == "BJT"):
    component_sorting.BJT(file_name)







   
# for row in spice_model:
    # print(row)
    #print(row[0])
#while spice_model.read() != None:
#  if()
