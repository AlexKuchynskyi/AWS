import boto3
import boto3.session
import json


user_profile = 'profile_name'
user_bucket = 'bucket_name'
list_objects_file = "s3bucket_create_multiple_objects.log"

# Setup a session for a specific CLI profile name,
# if only default profile is used - two below lines of code can be substituted to:
# s3 = boto3.client('s3')
my_session = boto3.session.Session(profile_name=user_profile)
s3 = my_session.client('s3')


log_file = open(list_objects_file, mode='w', encoding='latin_1')

for i in range(1, 1010):
    response = s3.put_object(
        Body='/path/to/file/test-file.txt',
        Bucket=user_bucket,
        Key="to_delete/test-file_" + str(i) + ".txt"
    )

    print(response)
    json_response = json.dumps(response)
    log_file.write(str(json_response))

log_file.close()
