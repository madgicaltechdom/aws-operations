import json
import boto3
import urllib3
import os


def response(status_code, body):
    return {"statusCode": status_code, "body": json.dumps(body)}


def get_instance_id_from_tags(event):
    params = event.get("queryStringParameters") or {}
    ec2 = boto3.client("ec2")
    filters = []

    if params.get("name"):
        filters.append({"Name": "tag:Name", "Values": [params["name"]]})

    if params.get("environment"):
        filters.append({"Name": "tag:environment", "Values": [params["environment"]]})

    if not filters:
        print("Missing instance tag query parameters", flush=True)
        return None, response(
            400,
            {
                "message": "Provide instance tags using query parameters, e.g. ?name=SonarQube&environment=qa"
            },
        )

    instances = ec2.describe_instances(Filters=filters)
    instance_ids = []

    for reservation in instances.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instance_ids.append(instance["InstanceId"])

    if len(instance_ids) != 1:
        print(f"Tag lookup did not resolve to one instance filters={filters} instance_ids={instance_ids}", flush=True)
        return None, response(
            400,
            {
                "message": f"Expected 1 instance for the provided tags, found {len(instance_ids)}",
                "instance_ids": instance_ids,
            },
        )

    print(f"Resolved instance_id={instance_ids[0]} filters={filters}", flush=True)
    return instance_ids[0], None


def getPublicIp(event, context):
    instance_id, error = get_instance_id_from_tags(event)
    if error:
        return error

    print(f"getPublicIp instance_id={instance_id}", flush=True)

    ec2 = boto3.client("ec2")
    instances = ec2.describe_instances(InstanceIds=[instance_id])
    instance = instances["Reservations"][0]["Instances"][0]
    public_ip = instance.get("PublicIpAddress")

    if not public_ip:
        return response(404, {"message": "No public IP address found for the instance"})

    return response(200, {"message": f"Instance public IP address is: {public_ip}", "instance_id": instance_id})


def manageInstance(event, context):
    params = event.get("queryStringParameters") or {}
    action = params.get("action", "").lower()

    if action not in ("start", "stop"):
        return response(400, {"message": "action must be start or stop"})

    instance_id, error = get_instance_id_from_tags(event)
    if error:
        return error

    print(f"manageInstance action={action} instance_id={instance_id}", flush=True)

    ec2 = boto3.client("ec2")
    if action == "start":
        ec2.start_instances(InstanceIds=[instance_id])
    else:
        ec2.stop_instances(InstanceIds=[instance_id])

    return response(200, {"message": f"Instance has been {action}ed", "instance_id": instance_id})


def post_message(url, message):
    data = {"text": message}
    http = urllib3.PoolManager()
    return http.request(
        "POST",
        url,
        headers={"Content-Type": "application/json"},
        body=json.dumps(data),
    )


def get_ses_quota(event, context):
    client = boto3.client("ses")

    body = client.get_send_quota()
    send_last_24_hrs = body["SentLast24Hours"]
    if (
        send_last_24_hrs / body["Max24HourSend"]
        >= float(os.getenv("WARN_LIMIT"))
    ):
        slack_url = os.getenv("SLACK_URL")
        if slack_url:
            post_message(slack_url, f"SES service is almost reaching the limit : {send_last_24_hrs}")
    return response(200, body)
