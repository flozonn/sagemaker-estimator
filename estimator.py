from sagemaker.estimator import Estimator
import sagemaker
import boto3

boto_session = boto3.Session(region_name='eu-central-1')
SESSION = sagemaker.Session(boto_session=boto_session)

# Define the Estimator
estimator = Estimator(
    image_uri="619071325606.dkr.ecr.eu-central-1.amazonaws.com/owkin-debug:latest",
    sagemaker_session=SESSION,
    #tags=DEFAULT_TAGS,
    role="SageMaker-sagemaker-role",
    instance_count=1,
    instance_type="ml.m5.large",
    base_job_name="simple-training-job",
    hyperparameters={"name": "my_own_name"},
    environment={
        "PYTHONUNBUFFERED": "1"  
    },
)


estimator.fit()