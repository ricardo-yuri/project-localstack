import boto3

client = boto3.client('sqs', endpoint_url='http://localhost.localstack.cloud:4566')

def send_sqs_message():
    response = client.send_message(
    QueueUrl='http://{os.environ.get("LOCALSTACK_HOST")/000000000000/product-queue',
    MessageBody='Capinha Iphone 14',
    DelaySeconds=123,
    MessageAttributes={},
    MessageSystemAttributes={},
    MessageDeduplicationId='',
    MessageGroupId='')
    return response

def send_message(event, context):
    response = send_sqs_message()
    return response