from boto3.session import Session

ACCESS_KEY_ID = 'ASIAZ7IG4XF7U7OX5WWS'
SECRET_KEY = 'Ksthh5Av7Mba7ByIXsk0q2XZn4OFal6SUoFSpxoF'
SESSION_TOKEN = 'FwoGZXIvYXdzEFsaDEkfraAX0v8M9ZlBQiLIAfjCfrvw2RQ9j62stAuaIykFJv/0HQk/QihlcbOrlgsDyi6swy0haYeCSnMh5xOQb+pj596oR3p/ipsuDN8qCcpAzhwTsJGNh2dl2KxFG7jASdhr5EbM39h9FMMi0GsItoHs6Xa82rOvBx8alQCwyVdpLTqfhRxwPK3ZXA/B3nTubHGrV4CCjVLaxolh4J0iJheZ4bxiYwF0YMIGfT+QWd3Mb02LZcgtEgGCRwTleN6nQe1EsHCONwXfR4auJVuguvJwn4VGiaQxKLXRoI0GMi01sxyx1Bb+MLB0L5+e927nbwved42CUEUbRQ9TFm+8U1E+FRnGqYilMd38cNo='


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
