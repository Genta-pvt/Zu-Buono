import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Zu-BuonoRecipe')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


def lambda_handler(event, context):
    title = event['Title']
    picture = event['Picture']
    material_1 = event['Material1']
    material_2 = event['Material2']
    material_3 = event['Material3']
    material_4 = event['Material4']
    material_5 = event['Material5']
    how_to = event['HowTo']
    contributor = event['Contributor']

    response = table.put_item(
        Item={
            'Title': title,
            'Picture': picture,
            'Material1': material_1,
            'Material2': material_2,
            'Material3': material_3,
            'Material4': material_4,
            'Material5': material_5,
            'HowTo': how_to,
            'Contributor': contributor,
        })
    return {
        'statusCode': 200,
        'body': json.dumps('Grazie! ' + contributor + '.', ensure_ascii=False)
    }
