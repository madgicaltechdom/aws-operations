AWS Operations
=======================================

This repository contains utility functions for AWS operations and it can be deployed using the Serverless Framework. Here is a [video demonstration](https://shorthillstech-my.sharepoint.com/:v:/p/kapil_jain/EX3JMNATCU1DvlyRIVYveHABgnVZ9nhWVKP0Z3zrcgnzWg?e=XpA4BN) of how to use this repository.

AWS Operations:
*   Get IP address of an instanceId e.g. `https://<serveless-endpoints>/?instance_id=<instanceId>`
*   Start an instanceId e.g. `https://<serveless-endpoints>/?instance_id=<instanceId>&action=start`
*   Stop an instanceId e.g. `https://<serveless-endpoints>/?instance_id=<instanceId>&action=stop`

Prerequisites
-------------

*   [AWS account and credentials set up on your local machine](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)
*   Node.js and npm installed
*   Serverless Framework installed (`npm install -g serverless`)

Setup
-----

1.  Clone this repository: `git clone https://github.com/madgicaltechdom/aws-operations.git`
2.  Navigate to the project directory: `cd aws-operations`
3.  Deploy the function to your AWS account using the Serverless Framework: `serverless deploy`
4. Copy the `endpoints url` from the output command line.

Usage
-----
You can invoke the endpoint using `https://<serveless-endpoints>/?instance_id=<instanceId>`

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
