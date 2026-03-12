import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

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

    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'short_code': short_code,
            'original_url': item['original_url'],
            'click_count': item['click_count'],
            'created_at': item['created_at']
        })
    }