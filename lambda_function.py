import pandas as pd

def lambda_handler(event, context):
    d = {'col1' : [1,2], 'col2': [4,5]}
    df = pd.DataFrame(data=d)
    print(df)
    print('done x1')