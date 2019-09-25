
STACK_NAME = roledemo

create-cfn:
	aws cloudformation create-stack --stack-name ${STACK_NAME} \
	  --capabilities CAPABILITY_NAMED_IAM \
	  --template-body file://demo-iam-roles-ssm.yml \
	  --parameters file://params.json

update-cfn:
	aws cloudformation update-stack --stack-name ${STACK_NAME} \
	  --capabilities CAPABILITY_NAMED_IAM \
	  --template-body file://demo-iam-roles-ssm.yml \
	  --parameters file://params.json
