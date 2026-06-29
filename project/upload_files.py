import boto3
import os

s3 = boto3.client('s3', region_name='ap-south-1')
bucket_name = "my-cloudsite-automator-12345"

content_types = {
    ".html": "text/html",
    ".css": "text/css"
}

print("Current folder:", os.getcwd())

for file in os.listdir("."):
    ext = os.path.splitext(file)[1]

    if ext in content_types:
        print("Uploading:", file)

        s3.upload_file(
            file,
            bucket_name,
            file,
            ExtraArgs={
                'ContentType': content_types[ext]
            }
        )

        print("Uploaded:", file)

print("Done")