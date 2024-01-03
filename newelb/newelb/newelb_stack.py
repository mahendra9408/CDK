from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_elasticloadbalancing as elb,
    aws_ec2 as ec2,
)
from constructs import Construct

class NewelbStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "newelb-vpc",
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
            )

        lb = elb.LoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True,
            health_check=elb.HealthCheck(
                port=80
            )
        )

        lb.add_listener(
            external_port=80
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "NewelbQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
