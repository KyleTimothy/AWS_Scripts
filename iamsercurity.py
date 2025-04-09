import boto3
from botocore.exceptions import ClientError
#kyle

def create_iam_user(username):
    """
    Create an IAM user with the specified username.
    """
    iam = boto3.client('iam')
    
    try:
        response = iam.create_user(UserName=username)
        print(f"User {username} created successfully.")
        return response
    except ClientError as e:
        print(f"Error creating user: {e}")
        return None
options = ["1. Create an IAM user", "2. Delete an IAM user", "3. List IAM users", "4. Get IAM user details", "5. Create an IAM group", "6. Delete an IAM group", "7. List IAM groups"]
print(options)
option = input("Which AWS CLI tool will you choose: ")


def create_iam_group(group_name):
    """
    Create an IAM group with the specified group name.
    """
    iam = boto3.client('iam')

    try:
        response = iam.create_group(GroupName=group_name)
        print(f"Group {group_name} created successfully.")
        return response
    except ClientError as e:
        print(f"Error creating group: {e}")
        return None
    
  

match option:
    case "1":
        createUser = input("Enter username to create: ")
        create_iam_user(createUser)
        print("IAM user created successfully.")

    case "2":
        deleteUser = input("Enter username to delete: ")
        iam = boto3.client('iam')
        
        try:
            response = iam.delete_user(UserName=deleteUser)
            print(f"User {deleteUser} deleted successfully.")
        except ClientError as e:
            print(f"Error deleting user: {e}")
    case "3":
        iam = boto3.client('iam')
        try:
            response = iam.list_users()
            print("List of IAM users:")
            for user in response['Users']:
                print(user['UserName'])
        except ClientError as e:
            print(f"Error listing users: {e}")

    case "4":
        iam = boto3.client('iam')
        try:
            response = iam.get_user()
            print("IAM user details:")
            print(response['User'])
        except ClientError as e:
            print(f"Error getting user details: {e}")
    case "5":
       createGroup = input("Enter group name to create: ")
       create_iam_group(createGroup)
       print("IAM group created successfully.")

    case "6":
        deleteGroup = input("Enter group name to delete: ")
        iam = boto3.client('iam')
        
        try:
            response = iam.delete_group(GroupName=deleteGroup)
            print(f"Group {deleteGroup} deleted successfully.")
        except ClientError as e:
            print(f"Error deleting group: {e}") 
    case "7":
            iam = boto3.client('iam')
            try:
             response = iam.list_groups()
             print("List of IAM groups:")
             for group in response['Groups']:
                print(group['GroupName'])
            except ClientError as e:
             print(f"Error listing groups: {e}")
