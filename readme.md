# Serverless Image Processing System




## Overview
This serverless application processes images uploaded via API Gateway. The system stores original images in S3, processes them through Lambda functions, stores processed versions in another S3 bucket, and tracks metadata in DynamoDB.

---

## Solution Architecture
![Architecture Diagram](Solution Architecture.png)
<img src="Solution Architecture.png" alt="Architecture Diagram" width="600" />


---

## Key Components
- **API Gateway:** Accepts image uploads
- **Upload Lambda:** Stores images and metadata
- **Processing Lambda:** Resizes and processes images
- **S3 Buckets:** Store original and processed images
- **DynamoDB:** Tracks image metadata
- **CloudWatch:** Monitors system operations

---
## Setup
### 1. Create S3 Buckets
### 2. Create DynamoDB Table
### 3. Create IAM Roles
- **Attach the following policy (see `policy.json`):**

### 4. Create lambda functions
- **create the upload lambda function (see `image upload lamdba.py`):**
- **create the upload lambda function (see `image processing lambda.mjs`):**

---

## API Usage
**Upload Image:**
```bash
  curl -X POST https://{api-id}.execute-api.{region}.amazonaws.com/prod/upload \
    -H "Content-Type: image/png" \
    --data-binary "@image.png"
```

---

## Monitoring
- Access logs in CloudWatch:
  - Upload Lambda: `/aws/lambda/ImageUploadHandler`
  - Processing Lambda: `/aws/lambda/ImageProcessingHandler`

---

## Notes
- Ensure all environment variables and resource names match your AWS setup.
- The provided code and policy are correct and match the described architecture.
- The policy in `policy.json` grants the required permissions for S3, DynamoDB, and CloudWatch logs.
- The Lambda functions are correct for their intended purpose.