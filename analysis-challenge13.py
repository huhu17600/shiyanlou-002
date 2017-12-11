import json
import pandas as pd

def analysis(file,user_id):
    if(file and user_id):
        df = pd.read_json(file)
        times = 0
        minutes = 0
        minutes = df[df['user_id']==user_id]['minutes'].sum()
        times = df[df['user_id']==user_id]['user_id'].count()
        return times,minutes
    else:
        return 0

if '__name__' == '__main__':
    data = analysis('/home/Code/user_study.json',199071)
    print('haha')
    print(data)
