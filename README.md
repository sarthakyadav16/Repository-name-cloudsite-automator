📘 CloudSite Automator
🚀 AWS S3 Static Website Hosting Automation using Python (boto3)
📌 Overview

CloudSite Automator is a Python-based automation project that deploys a static website to Amazon S3 using the AWS SDK (boto3).

It automates the complete workflow:

Creating an S3 bucket
Enabling static website hosting
Uploading website files (HTML/CSS/JS)
Setting bucket policy for public access
Generating a live website URL


🎯 Features
⚡ Fully automated S3 bucket creation
🌐 Static website hosting setup
📂 Bulk file upload using Python
🔓 Automatic public access configuration
🔗 Instant website URL generation
🧠 Beginner-friendly AWS automation project


🧰 Tech Stack
Python 🐍
AWS S3 ☁️
boto3 (AWS SDK for Python)


📁 Project Structure
CloudSite-Automator/
│
├── project/
│   ├── index.html
│   ├── error.html
│   ├── style.css
│
├── main.py
├── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/CloudSite-Automator.git
cd CloudSite-Automator

2️⃣ Install Dependencies
pip install boto3

3️⃣ Configure AWS Credentials
aws configure

Provide:

AWS Access Key ID
AWS Secret Access Key
Region (e.g., ap-south-1)
Output format (json)

4️⃣ Run the Project
python main.py
🌍 Output

After successful execution, you will get a live website URL like:

http://your-bucket-name.s3-website.ap-south-1.amazonaws.com


🧠 How It Works
Creates S3 bucket using boto3
Enables static website hosting
Uploads website files automatically
Applies public read policy
Generates live website link
📸 Example Output
Bucket created successfully
Static website hosting enabled
Files uploaded successfully
Website URL: http://cloudsite-automator.s3-website.ap-south-1.amazonaws.com


🔥 Future Improvements
CI/CD integration with GitHub Actions
CloudFront + HTTPS support
Custom domain mapping
Drag-and-drop deployment UI

👨‍💻 Author
Sarthak Yadav

⭐ If you like this project

Give a ⭐ on the repository and feel free to contribute!
