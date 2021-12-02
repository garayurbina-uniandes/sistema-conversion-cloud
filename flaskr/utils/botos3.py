from boto3.session import Session
import os

ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
SECRET_KEY = os.environ['SECRET_KEY']
SESSION_TOKEN = os.environ['SESSION_TOKEN']


session = Session(aws_access_key_id=ACCESS_KEY_ID,
                    aws_secret_access_key=SECRET_KEY,
                    aws_session_token=SESSION_TOKEN)

s3 = session.resource('s3')
bucket = 'sistema-conversion-cloud-grupo-16'
my_bucket = s3.Bucket(bucket)

def download_from_s3(fileKey,fileDestination):
    my_bucket.download_file(fileKey, fileDestination)

def upload_to_s3(fileLocation,fileKey):
    my_bucket.upload_file(fileLocation, fileKey)
