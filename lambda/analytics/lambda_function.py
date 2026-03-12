import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PASTE_YOUR_TABLE_NAME')

def convert_decimal(obj):
    if isinstance(obj, list):
        return [convert_decimal(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return int(obj)
    else:
        return obj

def lambda_handler(event, context):

    short_code = event['pathParameters']['code']

    response = table.get_item(
        Key={'short_code': short_code}
    )

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'URL not found'})
        }

    item = convert_decimal(response['Item'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'short_code': short_code,
            'original_url': item['original_url'],
            'click_count': item['click_count'],
            'created_at': item['created_at']
        })
    }