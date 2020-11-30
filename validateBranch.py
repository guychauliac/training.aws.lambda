import json


def validate(event, context):
    body = {
        true
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response