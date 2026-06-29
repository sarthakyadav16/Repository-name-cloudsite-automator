# Step 1: Your bucket name
bucket_name = "my-cloudsite-automator-12345"

# Step 2: Generate website URL
website_url = f"http://{bucket_name}.s3-website.ap-south-1.amazonaws.com"

# Step 3: Print URL
print("Your website is live at:")
print(website_url)