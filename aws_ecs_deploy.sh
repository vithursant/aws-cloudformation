aws cloudformation create-stack \
  --stack-name AmazonECSLinuxTestFourStack \
  --template-body file://aws_ecs.yml \
  --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=KeyName,ParameterValue=vt_key \
    ParameterKey=SSHLocation,ParameterValue=207.245.12.90/32 \
    ParameterKey=VpcId,ParameterValue=vpc-e89b8f8c \
    ParameterKey=Subnets,ParameterValue=subnet-05083761
