## 🧾 Project Development Summary

### 1. Repository Setup
I began by forking the original GitHub repository and cloning it to my local machine to begin development.

### 2. CI/CD Integration
I created an account on [Travis CI](https://travis-ci.com/) and linked it to my GitHub account to enable automated builds and deployments.

### 3. Flask Application Development
I developed the core Flask application along with its routing logic using Python. To streamline development, I installed the required libraries locally and worked within the PyCharm IDE.

### 4. Configuration and Containerization
After verifying the app’s functionality, I created a `.env` file to store environment variables and wrote a `Dockerfile` to containerize the application. Once the image build was successful, I created a `docker-compose.yml` file for easier orchestration.

### 5. Testing
I implemented unit tests using `pytest` and ensured they executed correctly in the local environment.

### 6. Travis CI Pipeline
Finally, I created a `.travis.yml` file to automate the CI/CD process. This pipeline runs the tests, builds the Docker image, and pushes it to Docker Hub upon successful execution.