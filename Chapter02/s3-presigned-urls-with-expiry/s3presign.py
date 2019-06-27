import boto3

boto3.setup_default_session(profile_name='awssecadmin')
s3_client = boto3.client('s3')

url = s3_client.generate_presigned_url('get_object', Params={'Bucket': 'awsseccookbook', 'Key': 'mission-impossible.txt'}, ExpiresIn=300)
print(url)
