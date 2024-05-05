 
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
An AWS lambda function that analyzes documents with Amazon Textract.
"""
import json
import base64
import logging
import boto3
import os

from botocore.exceptions import ClientError

# Set up logging.
logger = logging.getLogger(__name__)
logger = logging.getLogger()
logger.setLevel("INFO")
# Get the boto3 client.
textract_client = boto3.client('textract')


def lambda_handler(event, context):
    """
    Lambda handler function
    param: event: The event object for the Lambda function.
    param: context: The context object for the lambda function.
    return: The list of Block objects recognized in the document
    passed in the event object.
    """
    try:
        # Determine document source.
        if 'image' in event:
            # Decode the image
            image = event['image']
        elif 'body' in event:
            # Decode the image
            new_string = ''.join(event['body'].split('\r\n'))
            new_dict = json.loads(new_string)
            image = new_dict['image']
        print(image)
        image_bytes = image.encode('utf-8')
        img_b64decoded = base64.b64decode(image_bytes)
        image = {'Bytes': img_b64decoded}

        if 'S3Object' in event:
            image = {'S3Object':
                     {'Bucket':  event['S3Object']['Bucket'],
                      'Name': event['S3Object']['Name']}
                     }


        # Analyze the document.
        response = textract_client.detect_document_text(Document=image)

        # Get the Blocks
        blocks = "Bir yazi okunamadi."
        #print(response['Blocks'])
        if (len(response['Blocks']) > 1):
            blocks = response['Blocks'][1]["Text"]
            #print('BLOCK BEGIN')
            #print(blocks)
            #print('BLOCK END')
        lambda_response = {
            "statusCode": 200,
            "body": json.dumps(blocks)
        }

    except ClientError as err:
        error_message = "Couldn't analyze image. " + \
            err.response['Error']['Message']

        lambda_response = {
            'statusCode': 400,
            'body': {
                "Error": err.response['Error']['Code'],
                "ErrorMessage": error_message
            }
        }
        logger.error("Error function %s: %s",
            context.invoked_function_arn, error_message)

    except ValueError as val_error:
        lambda_response = {
            'statusCode': 400,
            'body': {
                "Error": "ValueError",
                "ErrorMessage": format(val_error)
            }
        }
        logger.error("Error function %s: %s",
            context.invoked_function_arn, format(val_error))

    return lambda_response
