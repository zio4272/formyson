import boto3
import os
import hashlib
import time

from rest_framework.response import Response

def post_image_s3_upload(image):

    aws_s3 = boto3.resource('s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    
    _, file_extension = os.path.splitext(image.name)

    file_name = 'post_images/{}_{}{}'.format(
        hashlib.md5('postimages'.encode('utf8')).hexdigest(),
        round(time.time() * 10000),
        file_extension)
    
    image_body = image.read()

    aws_s3.Bucket(os.environ.get('AWS_BUCKET_NAME'))\
        .put_object(Key=file_name, Body=image_body)

    aws_s3\
        .ObjectAcl(os.environ.get('AWS_BUCKET_NAME'), file_name)\
        .put(ACL='public-read')

    return Response('{}'.format(file_name))