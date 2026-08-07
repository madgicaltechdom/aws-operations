AWS Operations
=======================================

This repository contains utility functions for AWS operations and it can be deployed using the Serverless Framework.

AWS Operations:
*   Get IP address of an instance using tags e.g. `https://<serveless-endpoints>/?name=SonarQube&environment=qa`
*   Start an EC2 instance using tags e.g. `https://<serveless-endpoints>/manageInstance?name=SonarQube&environment=qa&action=start`
*   Stop an EC2 instance using tags e.g. `https://<serveless-endpoints>/manageInstance?name=SonarQube&environment=qa&action=stop`
*   Start an EC2 Fleet using tags e.g. `https://<serveless-endpoints>/manageFleet?name=SonarQube&environment=qa&action=start`
*   Stop an EC2 Fleet using tags e.g. `https://<serveless-endpoints>/manageFleet?name=SonarQube&environment=qa&action=stop`
*   Check SES Quota e.g.  `https://<serveless-endpoints>/getSESQuota`

The `name` query parameter maps to the EC2 tag key `Name`. The `environment` query parameter maps to the EC2 tag key `environment`.

**Note:** EC2 Fleet start/stop works by modifying the fleet's target capacity. Stop sets capacity to 0 (terminates instances), start sets it back to 1 (launches new instances). With one-time Spot requests, the instance ID changes on each start.

**Note:** Fleet tag lookup only matches fleets in the `active` or `modifying` state. Deleted/cancelled fleet records (retained by AWS for up to 48 hours) are ignored, so multiple fleets sharing the same tags do not cause conflicts.

Prerequisites
-------------

*   [AWS account and credentials set up on your local machine](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)
*   Node.js and npm installed
*   Serverless Framework installed (`npm install -g serverless`)
*   Enable [Slack webhook](https://api.slack.com/messaging/webhooks) and update SLACK_URL variable in serverless.yml

Setup
-----

1.  Clone this repository: `git clone https://github.com/madgicaltechdom/aws-operations.git`
2.  Navigate to the project directory: `cd aws-operations`
3.  Deploy the function to your AWS account using the Serverless Framework: `serverless deploy`
4. Copy the `endpoints url` from the output command line.

Usage
-----

You can invoke the endpoint using tags: `https://<serveless-endpoints>/?name=SonarQube&environment=qa`

You can invoke the Lambda function using the Serverless Framework: `serverless invoke --function getPublicIp --path data.json`

You can also test the function by calling the endpoint that is created when you deploy the function. This endpoint will be shown in the output of the `serverless deploy` command.

Configuration
-------------

You can configure the function and the events that trigger it in the `serverless.yml` file.

Contributing
------------

We welcome contributions to this repository. Please submit a pull request with your changes and we will review them as soon as possible.

License
-------

This project is licensed under the MIT License.
