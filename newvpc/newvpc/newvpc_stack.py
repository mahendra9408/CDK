from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
)
from constructs import Construct

class NewvpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "newvpc")
        subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)],
        [ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)],
        [ec2.SubnetConfiguration(name="private",subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)],
        [ec2.SubnetConfiguration(name="private",subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)],
        nat_gateways=2,
        availability_zones=2

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "NewvpcQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
