import aws_cft_deploy

if __name__ == "__main__":
	deployInstance = aws_cft_deploy.DeployEC2Instance()
	deployInstance.main()