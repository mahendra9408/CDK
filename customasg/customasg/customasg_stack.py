from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_autoscaling as asg,
    aws_ec2 as ec2,
)
from constructs import Construct

class CustomasgStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "mycustom-vpc",
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
            )

        my_security_group = ec2.SecurityGroup(self, "mycustom-sg", vpc=vpc)
        asg.AutoScalingGroup(self, "mycustom-asg",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(),
            security_group=my_security_group,
            min_capacity=2,
            max_capacity=5
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CustomasgQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
