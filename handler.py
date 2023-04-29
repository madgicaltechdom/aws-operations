import json
import boto3

def getPublicIp(event, context):
    ec2 = boto3.client('ec2')
    instance_id = 'i-0f61caec55a2c3103'
    response = ec2.describe_instances(InstanceIds=[instance_id])
    ip_address = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return ip_address

def manageInstance(event, context):
    ec2 = boto3.client('ec2')
    instance_id = 'i-0f61caec55a2c3103'
    action = event['action']
    if action == 'start':
        ec2.start_instances(InstanceIds=[instance_id])
        return 'Instance started'
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        return 'Instance stopped'
    else:
        return 'Invalid action'
