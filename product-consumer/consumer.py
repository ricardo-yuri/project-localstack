import boto3

endpoint_url = 'http://localhost.localstack.cloud:4566'
endpoint_url_queue = endpoint_url + '/000000000000/product-queue'

client = boto3.client('sqs', endpoint_url='http://localhost.localstack.cloud:4566')
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost.localstack.cloud:4566')

response = client.receive_message(
    QueueUrl= endpoint_url_queue,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
messageBody = message['Body']
receipt_handle = message['ReceiptHandle']

print('Received message: %s' % messageBody)

def receive_message(event, context):
    message = 'Nome do produto que será salvo na base noSql dynamoDB'  
    return { 
        'message' : message + ' ' + messageBody
    }