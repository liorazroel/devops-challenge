# devops-challenge instructions

This project is a proof-of-concept (POC) application for securely extracting a secret string from a DynamoDB table in AWS.

## 📦 Prerequisites

Before running this project, ensure the following tools are installed on your system:

- [Python 3.12+](https://www.python.org/downloads/release/python-3120/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/liorazroel/devops-challenge.git
cd devops-challenge
```

### 2. Create a Virtual Environment and install dependencies
```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
```commandline
AWS_ACCESS_KEY_ID=<your_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
AWS_REGION=<your_aws_region>
CODE_NAME=<your_code_name>
GITHUB_PROJECT=<your_github_project>
LINK_TO_DOCKER_HUB=<your_docker_hub_link>
```
### Run the Flask Application
```bash
python app/app.py
```

### Run the pytest
```bash
PYTHONPATH=./app pytest
```
