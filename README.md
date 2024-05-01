# kelimem_dogru_mu

https://davidwalsh.name/browser-camera

C:\Users\your_windows_username\\.aws
contains

config file as:

[default]
region = [your_region]

credential file as:

[default]

aws_access_key_id = your_aws_access_key_id

aws_secret_access_key = your_aws_secret_access_key


[your_user_name]
# This key identifies your AWS account.
aws_access_key_id = your_aws_access_key_id
# Treat this secret key like a password. Never share it or store it in source
# control. If your secret key is ever disclosed, immediately use IAM to delete
# the key pair and create a new one.
aws_secret_access_key = your_aws_secret_access_key


Example call:
python client.py detect_text s3://detect-text-bucket/basit.jpg