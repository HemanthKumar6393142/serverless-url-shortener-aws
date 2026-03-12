import json
import boto3
import random
import string
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    body = json.loads(event['body'])
    original_url = body['url']

    short_code = generate_short_code()

    table.put_item(
        Item={
            'short_code': short_code,
            'original_url': original_url,
            'created_at': datetime.utcnow().isoformat(),
            'click_count': 0
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'short_code': short_code
        })
    }