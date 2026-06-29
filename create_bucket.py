import boto3

# Step 1: Create S3 client
s3 = boto3.client('s3')

# Step 2: Bucket name (must be unique globally)
bucket_name = "my-cloudsite-automator-12345"

# Step 3: Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket created successfully:", bucket_name)