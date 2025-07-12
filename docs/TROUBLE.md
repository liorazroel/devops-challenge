## 🐞 Troubleshooting: DynamoDB `get-item` Key Schema Error

1. While trying to retrieve the secret code from the DynamoDB table, I encountered an issue due to incorrect key casing.

### ❌ Attempted Command
```bash
aws dynamodb get-item \
  --table-name devops-challenge \
  --key '{"code_name": {"S": "thedoctor"}}'
 ```

An error occurred (ValidationException) when calling the GetItem operation: The provided key element does not match the schema

DynamoDB key attribute names are case-sensitive. The task stated:
codeName = thedoctor
After testing a few variations, I corrected the key name to match the case exactly:
```bash
aws dynamodb get-item \
  --table-name devops-challenge \
  --key '{"codeName": {"S": "theDoctor"}}'
```

2. ### ❌ Travis CI Build Trigger Issue
I couldn't trigger any builds on Travis CI. The workflows never started after pushing to GitHub or updating the repository.

### 🔍 Root Cause
Travis CI recently disable its free Continuous Integration (CI) offerings for open source and personal projects. A paid plan is now required to activate CI builds for new repositories.<br>
https://docs.travis-ci.com/user/billing-overview/

3. ## 🐍 Troubleshooting: `ModuleNotFoundError` During Unit Testing (PYTHONPATH Issue)

### ❌ Problem
When running unit tests with `pytest`, I encountered import errors like:
ModuleNotFoundError: No module named ‘router’
This happened even though the `router.py` file exists inside the `app/` folder.

### 🧠 Root Cause
Python couldn’t resolve the relative module imports because the `PYTHONPATH` wasn’t set to include the `app/` directory. By default, Python only includes the current directory (`.`), not nested folders like `app/`.

### ✅ Solution
I updated the test command to explicitly set the `PYTHONPATH`:

```bash
PYTHONPATH=./app pytest
