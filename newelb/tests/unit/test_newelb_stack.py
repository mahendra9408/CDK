import aws_cdk as core
import aws_cdk.assertions as assertions

from newelb.newelb_stack import NewelbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in newelb/newelb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NewelbStack(app, "newelb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
