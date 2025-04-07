import boto3
from botocore.exceptions import ClientError

options = ["1. S3 Viewing Buckets", "2. Deleting buckets", "3. Creating an EC2 instance", "4. Deleting an Instance", "5. Creating an S3 Bucket", "6. Delete multiple instances"]
print(options)
lang = input("Which AWS CLI tool will you choose: ")

def create_ec2_instance(instance_type, key_name, security_group_ids, ami_id):
    ec2 = boto3.resource('ec2')
    try:
        instance = ec2.create_instances(
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            ImageId=ami_id,
            MinCount=1,
            MaxCount=1
        )
        print(f"EC2 instance created with ID: {instance[0].id}")
    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")

def create_ec2_instances(instance_type, key_name, security_group_ids, ami_id, instance_count):
    ec2 = boto3.resource('ec2')
    try:
        instances = ec2.create_instances(
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            ImageId=ami_id,
            MinCount=instance_count,
            MaxCount=instance_count
        )
        print(f"EC2 instance created with ID: {instance[0].id}")
    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")


def delete_ec2_instance(instance_id):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Termination initiated for instance ID: {instance_id}")
        for instance in response['TerminatingInstances']:
            print(f"Instance {instance['InstanceId']} is now in state: {instance['CurrentState']['Name']}")
    except ClientError as e:
        print(f"Error deleting EC2 instance: {e}")

def delete_ec2_instances(instance_ids):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.terminate_instances(InstanceIds=instance_ids)
        print(f"Termination initiated for instances: {', '.join(instance_ids)}")
        for instance in response['TerminatingInstances']:
            print(f"Instance {instance['InstanceId']} is now in state: {instance['CurrentState']['Name']}")
    except ClientError as e:
        print(f"Error deleting EC2 instances: {e}")

match lang:
    case "1":
        print("View S3 Buckets")
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    case "2":
        s3 = boto3.client('s3')
        bucket_name = input("Enter the bucket name to delete: ")
        try:
            s3.delete_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting bucket: {e}")
    case "3":
        instance_type = input("Enter the EC2 instance type (e.g., t2.micro): ")
        key_name = input("Enter the name of the key pair: ")
        security_group_ids = input("Enter the security group IDs (comma-separated): ").split(',')
        ami_id = input("Enter the AMI ID: ")
        create_ec2_instance(instance_type, key_name, security_group_ids, ami_id)
    case "4":
        instance_type = input("Enter the EC2 instance type (e.g., t2.micro): ")
        key_name = input("Enter the name of the key pair: ")
        security_group_ids = input("Enter the security group IDs (comma-separated): ").split(',')
        ami_id = input("Enter the AMI ID: ")
        instance_count = int(input("Enter the number of instances to create: "))

        create_ec2_instances(instance_type, key_name, security_group_ids, ami_id)    
    case "5":
        action = input("Do you want to create or delete an EC2 instance? (create/delete): ").strip().lower()
        if action == "create":
            instance_type = input("Enter the EC2 instance type (e.g., t2.micro): ")
            key_name = input("Enter the name of the key pair: ")
            security_group_ids = input("Enter the security group IDs (comma-separated): ").split(',')
            ami_id = input("Enter the AMI ID: ")
            instance_count = int(input("Enter the number of instances to create: "))
            create_ec2_instances(instance_type, key_name, security_group_ids, ami_id, instance_count)
        elif action == "delete":
            instance_id = input("Enter the EC2 instance ID to delete: ")
            delete_ec2_instance(instance_id)
        else:
            print("Invalid action. Please choose 'create' or 'delete'.")
    case "6":
        action = input("Do you want to create or delete EC2 instances? (create/delete): ").strip().lower()
        if action == "create":
            instance_type = input("Enter the EC2 instance type (e.g., t2.micro): ")
            key_name = input("Enter the name of the key pair: ")
            security_group_ids = input("Enter the security group IDs (comma-separated): ").split(',')
            ami_id = input("Enter the AMI ID: ")
            instance_count = int(input("Enter the number of instances to create: "))