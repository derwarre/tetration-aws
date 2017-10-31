import boto3
import json
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
groups = ec2client.describe_security_groups()

print(groups['SecurityGroups'][3]['GroupId'])
#print response
for instance in response["Reservations"][0]["Instances"]:
    print(instance['InstanceId'] + ' -- ' + instance['PrivateIpAddress'])
    ec2client.modify_instance_attribute(
    DryRun=False,
    InstanceId=instance['InstanceId'],
    Groups=[
        groups['SecurityGroups'][0]['GroupId']
    ])

#    if group['GroupName'] != 'default':
#        print(group['GroupName'] + " - " + group['GroupId'] +  " - " + str(len(group['IpPermissions'])))
#        if len(group['IpPermissions']) > 0:
#            response2 = ec2client.revoke_security_group_ingress(
#            DryRun=False,
#            GroupId=group['GroupId'],
#            IpPermissions=group['IpPermissions'])
            #print(response2)
