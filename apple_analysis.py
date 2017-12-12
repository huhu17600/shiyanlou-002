# -*- coding:utf-7 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    data2 = pd.to_datetime(data.Date)
    data.Volume.index = data2
    data1 = data.Volume
    data4 = data1.resample('3M').sum().sort_values()
    data3 = data1.resample('Q').sum().sort_values()
    second_volume = data3[-2]
    print(data1)
    print(data3)
    print(data4)
    return second_volume
if __name__ == '__main__':
    quarter_volume()
