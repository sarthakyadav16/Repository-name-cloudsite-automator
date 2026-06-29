import boto3

bucket_name = "my-cloudsite-automator-12345"

s3 = boto3.client('s3')

website_configuration = {
    'IndexDocument': {
        'Suffix': 'index.html'
    },
    'ErrorDocument': {
        'Key': 'error.html'   # ✅ MUST be "Key" (capital K)
    }
}

s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
)

print("Static website hosting enabled")