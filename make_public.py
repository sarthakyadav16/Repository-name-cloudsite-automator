import boto3
import json

# Step 1: Connect to S3
s3 = boto3.client('s3')

# Step 2: Your bucket name
bucket_name = "my-cloudsite-automator-12345"

# Step 3: Bucket policy (public access)
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

# Step 4: Apply policy to bucket
s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(bucket_policy)
)

# Step 5: Confirmation message
print("Bucket is now public")