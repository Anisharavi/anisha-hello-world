import json
import boto3
import botocore
import logging
logging.getLogger().setLevel(logging.INFO)
s3 = boto3.resource('s3')
BUCKET_NAME="dev-days-test"
KEY="hello.txt"

def wish_hello_world_handler(event, context):

    logging.info(event)
    # TODO implement
    
    try:
        s3.Bucket(BUCKET_NAME).downloads_file(KEY, '/tmp/hello_local.txt')
    except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                logging.error("The object doesnot exist")
            else:
                 raise 
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
