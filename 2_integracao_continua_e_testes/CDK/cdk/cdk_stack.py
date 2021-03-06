from aws_cdk import core
from aws_cdk import aws_s3 as s3


class CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        s3.Bucket(self, 'bucket-s3-cdk-iac',bucket_name='bucket-s3-cdk-iac')

        # The code that defines your stack goes here
