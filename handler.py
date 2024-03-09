import json
import boto3
import urllib3
import os


def getPublicIp(event, context):

    instance_id = 'i-0f0ae101cf8e3202e'  # This is the instance ID from the event
    ec2 = boto3.client('ec2')
    if 'queryStringParameters' in event:
        instance_id = event['queryStringParameters']['instance_id']

    instances = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = instances['Reservations'][0]['Instances'][0]['PublicIpAddress']
    body = {
        "message": f"Instance public IP address is: {public_ip}"
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def manageInstance(event, context):

    ec2 = boto3.client('ec2')
    action = 'start'

    if 'queryStringParameters' in event:
        instance_id = event['queryStringParameters']['instance_id']
        action = event['queryStringParameters']['action']
        print(f"{instance_id} {action}")
        if action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])

    body = {
        "message": f"Instance has been {action}ed"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def get_ses_quota(event, context):

    client = boto3.client('ses')

    body = client.get_send_quota()
    send_last_24_hrs = body["SentLast24Hours"]
    if ((send_last_24_hrs/ body["Max24HourSend"]) >= float(os.getenv('WARN_LIMIT'))) :
        post_message(os.getenv('SLACK_URL'), f"SES service is almost reaching the limit : {send_last_24_hrs}")
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# def post_message(url, message):
#     """Post a message to slack using a webhook url."""
#     data = {'text': message}
#     http = urllib3.PoolManager()
#     resp = http.request('POST', url,
#              headers={'Content-Type': 'application/json'},
#              body=json.dumps(data))
#     return {"statusCode": resp.status, "body": json.dumps(body)}
