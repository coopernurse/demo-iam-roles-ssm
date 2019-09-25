#!/usr/bin/env python

import boto3

#
# get credentials via ssm
ssm_client = boto3.client("ssm")
resp = ssm_client.get_parameters(WithDecryption=True, Names=[
    "/config/roledemo/component/aws/accesskey",
    "/config/roledemo/component/aws/secretkey"
    ])
access_key = [ p["Value"] for p in resp["Parameters"] if p["Name"].endswith("accesskey") ][0]
secret_key = [ p["Value"] for p in resp["Parameters"] if p["Name"].endswith("secretkey") ][0]
print access_key, secret_key

#
# create sqs client with credentials
sqs_client = boto3.client("sqs", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
queues = sqs_client.list_queues()
for q in queues["QueueUrls"]:
    print q

