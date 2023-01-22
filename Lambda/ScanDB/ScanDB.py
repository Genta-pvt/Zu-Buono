import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Zu-BuonoRecipe')


def lambda_handler(event, context):
    response = table.scan(AttributesToGet=['Title', 'Contributor'])
    return {
        'statusCode': 200,
        'body': json.dumps(response, ensure_ascii=False)
    }
