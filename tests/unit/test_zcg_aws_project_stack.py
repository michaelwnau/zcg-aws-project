import aws_cdk as core
import aws_cdk.assertions as assertions

from zcg_aws_project.zcg_aws_project_stack import ZcgAwsProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in zcg_aws_project/zcg_aws_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ZcgAwsProjectStack(app, "zcg-aws-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
