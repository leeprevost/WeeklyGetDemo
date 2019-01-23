import json
import datetime
import pandas as pd


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
        
    }
    return {'statusCode': 200,
            'body': pd.DataFrame.from_dict(data),
            'headers': {'Content-Type': 'application/json'}}
