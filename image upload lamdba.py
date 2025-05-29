import json
import base64
import boto3
import uuid

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

def lambda_handler(event, context):
    try:
        # Decode binary data
        if event.get('isBase64Encoded'):
            image_data = base64.b64decode(event['body'])
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Expected base64-encoded binary data'})
            }

        # Generate unique ID
        image_id = str(uuid.uuid4())

        # Get size of the image
        size = len(image_data)  # size in bytes

        # Save image to S3
        filename = f"{image_id}.png"  # or your preferred extension
        s3.put_object(
            Bucket='source-bucket',
            Key=filename,
            Body=image_data,
            ContentType='image/png'
        )

        # Save metadata to DynamoDB
        table.put_item(
            Item={
                'imageId': image_id,
                'FileName': filename,
                'SizeBytes': size
            }
        )

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'image_id': image_id,
                'file_name': filename,
                'size_bytes': size
            })
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }