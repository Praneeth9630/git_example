import boto3

client = boto3.client('ec2')
response = client.run_instances(
 ImageId='ami-04e5276ebb8451442' ,
 InstanceType='t2.micro' ,
 KeyName='testing_KP' ,
 MaxCount=D2,
 MinCount=1,
)
