# Secure-AWS-Storage
Final Version of Fall Semester (2020-2021) Project in the Course - Cryptography and Network Security

From facilitating remote access to data to the digitalization of the education system, cloud technology has touched our lives in more ways than we could ever realize. However, cloud computing also presents some unique security challenges such as the third party adversaries accessing/manipulating the client data that requires to be addressed.

Cloud Cryptography uses encryption techniques to protect data used or stored in the Cloud. Data hosted by cloud providers is encrypted, allowing users to access shared cloud services securely, protecting sensitive data without delay in the delivery of information, beyond their corporate IT environment. We've demonstrated the aforementioned concept using the AWS Cloud with AES 256-bit encryption.

## Deployment (on Windows)
Download Project Code
```bash
git clone https://github.com/tanvipenumudy/Secure-AWS-Storage.git
```
Deploy Virtual Environment 
```
python -m venv project_env
project_env\Scripts\activate.bat
```
Install Requirements
```bash 
pip install -r requirements.txt
```
Deploy SQLite Database
```python
from app import db, create_app
db.create_all(app=create_app())
```
AWS Credentials Setup
```
aws configure list
aws configure
```
Run Flask Application
```
python directory\app.py
```
