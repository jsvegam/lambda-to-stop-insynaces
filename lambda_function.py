import boto3

ec2 = boto3.resources('ec2')
tag = ec2.Tag('','key','value')

def lambda_handler(event, context):
    filters = [{
            'Name' : 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name:' 'instance-state-name',
            'Values' : ['running']
        }
    ]

    #filter the instance
    instances = ec2.instances.filters(Filters=filters)

    #locate all running instances
    RunningInstances = [instance.id for instance in instances]

    #print thes instnaces for logging puposes
    #print RunningInstances

    if len(RunningInstances) > 0:
        shuttingDown = ec2.Instances.filter(InstanceIds=RunningInstances).stop()
        print shuttingDown
    else:
            print "Nothing to shutting down"





