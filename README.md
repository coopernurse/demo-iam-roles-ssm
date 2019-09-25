
# IAM CFN Role Demo

## Overview

This CFN template creates:

* EC2 instance assuming a IAM role that allows SSM parameter store reads
* IAM user with a policy that allows SQS operations
* IAM access key for above user
* SSM parameters for the access key / secret (encrypted)

`ssm_demo.py` shows how to fetch the credentials from SSM and then
use those credentials to create a 2nd client that can talk to SQS.

The idea is that each service in your system would have a unique
IAM user / access key pair and that services would load the credentials
from SSM at startup and use those creds when talking to AWS services.

In theory this stack should be checked in / maintained by the developers
writing the services and should be used with the local dev account during
development.

## Create config

Create a `params.json` file

```json
[
  {
    "ParameterKey": "SSHKeyName",
    "ParameterValue": "fixme"
  },
  {
    "ParameterKey": "VPC",
    "ParameterValue": ""
  },
  {
    "ParameterKey": "Subnet",
    "ParameterValue": ""
  }
]
```

## Create stack

```bash
$ export AWS_PROFILE=xyz
$ make create-cfn
```

Login to AWS console and get IP addr of ec2 host.

## Copy script to host

## Run script

```
$ ssh ec2-user@ipaddr

# on host
$ export AWS_DEFAULT_REGION=us-west-2
$ sudo yum install -y python-pip
$ sudo pip install boto3
$ python ssm_demo.py
```
