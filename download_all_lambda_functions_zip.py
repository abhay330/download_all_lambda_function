import boto3
import wget

session = boto3.Session(profile_name='myprofile') #Update with profile name you have for your account at .aws/credentials location

lambda_client = session.client('lambda') # Make sure you have define region as well at in your profile definition

paginator = lambda_client.get_paginator('list_functions')
response_iterator = paginator.paginate()

for response in response_iterator:
  functions = response["Functions"]

  for function in functions:
    function_name = str(function["FunctionName"])
    
    resp_gf = lambda_client.get_function(
        FunctionName=function_name
    )

    code_location = resp_gf['Code']['Location']
    filename = wget.download(code_location, out=f"{function_name}.zip")

    print(f"Downloaded file : {filename} ") # Will download the zip wth function name in present working directory
