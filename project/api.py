import boto3
import time
from serverless_utils.aws.stack import stack_output


STACK_NAME = 'itay-test-stack'
sqs = boto3.resource('sqs')

queue1 = sqs.Queue(stack_output(STACK_NAME, 'Queue1Url'))
queue2 = sqs.Queue(stack_output(STACK_NAME, 'Queue2Url'))
queue3 = sqs.Queue(stack_output(STACK_NAME, 'Queue3Url'))


def handler1(event, context):
    for m in event['Records']:
        print(m)
        #time.sleep(2)
        queue2.send_message(
            MessageBody='BODY QUEUE 1',
        )


def handler2(event, context):
    for m in event['Records']:
        print(m)
        #time.sleep(2)
        queue3.send_message(
            MessageBody='BODY QUEUE 2',
        )
