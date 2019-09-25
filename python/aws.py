import boto3
from botocore.exceptions import ClientError

ec2=boto3.resource('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
    for i in response:
        if(i.authorize_ingress(IpPermissions{IpRanges[CidrIp]}) == '0.0.0.0/0'):
            print ("Security Group %s is open to work",i.id)

except ClientError as e:
    print(e)