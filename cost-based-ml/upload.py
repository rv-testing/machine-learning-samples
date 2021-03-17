import boto3

client = boto3.client(
    's3',
    #aws_access_key_id='',
    #aws_secret_access_key=''
    #aws_session_token=SESSION_TOKEN
)
s3 = boto3.resource('s3')
data = open('ps.txt', 'rb')
s3.Bucket('ric07s3').put_object(Key='ps.txt', Body=data)

