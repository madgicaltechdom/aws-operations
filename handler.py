import json
import boto3


def getPublicIp(event, context):

    instance_id = 'i-0f0ae101cf8e3202e' # This is the instance ID from the event
    ec2 = boto3.client('ec2',region_name='us-east-2')
    if 'queryStringParameters' in event:
        instance_id = event['queryStringParameters']['instance_id']

    instances = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = instances['Reservations'][0]['Instances'][0]['PublicIpAddress']
    body = {
        "message": f"Instance public IP address is: {public_ip}"
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
