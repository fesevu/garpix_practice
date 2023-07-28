import json
import statistics
import pandas as pd
import csv

def data_preparation(data):
    widthList = []
    heightList = []
    lengthList = []
    volumeList = []
    countStacking = 0
    countTurnover = 0
    boxesCount = 0
    for x in data['data_result']['boxes']:
        widthList.append(x['size']['width'])
        heightList.append(x['size']['height'])
        lengthList.append(x['size']['length'])
        volumeList.append(x['size']['width']*x['size']['height']*x['size']['length'])
        if x['stacking'] == True:
            countStacking += 1
        if x['turnover'] == True:
            countTurnover += 1
        boxesCount += 1
    meanWidth = statistics.mean(widthList)
    meanHeight = statistics.mean(heightList)
    meanLength = statistics.mean(lengthList)
    meanVolume = statistics.mean(volumeList)

    loadingWidth = data['data_result']['cargo_space']['loading_size']['width']
    loadingHeight = data['data_result']['cargo_space']['loading_size']['height']
    loadingLength = data['data_result']['cargo_space']['loading_size']['length']

    density_percent = data['data_result']['cargo_space']['calculation_info']['density_percent']

    values = [meanWidth, meanHeight, meanLength, meanVolume, countStacking,
              countTurnover, boxesCount, loadingWidth, loadingHeight,
              loadingLength]
    columns = ['meanWidth','meanHeight','meanLength','meanVolume','countStacking',
           'countTurnover', 'boxesCount', 'loadingWidth', 'loadingHeight',
           'loadingLength']
    
    filename = 'df.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerow(values)

    df = pd.read_csv('df.csv')
    return df