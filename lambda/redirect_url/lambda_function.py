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
    original_url = item['original_url']

    table.update_item(
        Key={'short_code': short_code},
        UpdateExpression="SET click_count = click_count + :inc",
        ExpressionAttributeValues={':inc': 1}
    )

    return {
        'statusCode': 302,
        'headers': {
            'Location': original_url
        }
    }