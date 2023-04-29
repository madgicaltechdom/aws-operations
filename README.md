AWS Operations- Add Serverless function to get Ipaddress or start/stop the machine.
=======================================

This repository contains utility functions for AWS operations and it can be deployed using the Serverless Framework. Here is a [video demonstration](https://shorthillstech-my.sharepoint.com/:v:/p/kapil_jain/EX3JMNATCU1DvlyRIVYveHABgnVZ9nhWVKP0Z3zrcgnzWg?e=XpA4BN) of how to use this repository.

AWS Operations:
*   Get IP address of an instanceId e.g. `https://<serveless-endpoints>/?instance_id=<instanceId>`
*   Start an instanceId e.g. `https://<serveless-endpoints>/manageInstance?instance_id=<instanceId>&action=start`
*   Stop an instanceId e.g. `https://<serveless-endpoints>/manageInstance?instance_id=<instanceId>&action=stop`

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

### Read the above instructions carefully before proceeding on the below steps.

## Here are the steps I followed to perform this task:

1. According to the prerequisites requested in the repo of this task, I first installed Nodejs and npm.

2. Then to install the serverless framework, I went to my terminal and wrote the following command npm install -g serverless.

3. After this, I cloned the given repo and navigated toward aws-operations.

4. I set up my AWS credentials on my local machine, which was previously provided to me.

Note(I wrote the code differently)

5. Now as I run the serverless deploy command, which created the end-point URL and function in the AWS console.

![Screenshot (79)](https://user-images.githubusercontent.com/89498168/233800664-dc5d43f2-7070-405a-8736-5853613165f6.png)

![Screenshot (83)](https://user-images.githubusercontent.com/89498168/233800679-61c06a39-4748-4506-affa-34e0faecaa4e.png)


6. Then I copied the endpoint URL to invoke the endpoint using https://<serveless-endpoints>/?instance_id=<instanceId> use it like this (https://5spyfcd30d.execute-api.ap-south-1.amazonaws.com/?instance_id=i-0f61caec55a2c3103), as a result, it fetched the IP address of the desired instance.


![Screenshot (81)](https://user-images.githubusercontent.com/89498168/233800565-f48b4bb4-6c42-437e-8902-02c632993f72.png)



7. Then I copied another endpoint url i.e https://<serveless-endpoints>/manageInstance?instance_id=<instanceId>&action=stop (https://5spyfcd30d.execute-api.ap-south-1.amazonaws.com/manageInstance?instance_id=i-0f61caec55a2c3103&action=stop), but it gave a different output rather than stopping the machine.

![Screenshot (82)](https://user-images.githubusercontent.com/89498168/233800575-f4543a90-bfa0-4b05-a4fa-29ed9bb54667.png)


8. After that I invoked lamdba function by using serverless frame work serverless invoke --function getPublicIp --path data.json

which fetched the IP address of the desired instance.

9. I also used the above framework to successfully stop a running machine.serverless invoke --function manageInstance --path data.json

![Screenshot (80)](https://user-images.githubusercontent.com/89498168/233800610-150047a0-e5c7-419c-b6f7-6a93ce7eabf8.png)

![Screenshot (84)](https://user-images.githubusercontent.com/89498168/233800620-a8c211d6-cd61-4c6c-a0b0-7f48f9e4eccf.jpg)


Contributing
------------

We welcome contributions to this repository. Please submit a pull request with your changes and we will review them as soon as possible.

License
-------

This project is licensed under the MIT License.
