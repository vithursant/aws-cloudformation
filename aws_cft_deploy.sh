aws cloudformation create-stack \
  --stack-name NVIDIAGPUDockerStack \
  --template-body file://aws_cft.json\
  --parameters ParameterKey=KeyName,ParameterValue=vt_key \
  	ParameterKey=InstanceType,ParameterValue=g2.2xlarge \
    	ParameterKey=SSHLocation,ParameterValue=207.245.12.90/32
