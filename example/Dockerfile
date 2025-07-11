FROM python:3.12-alpine
WORKDIR /devops-challenge
COPY app /devops-challenge/app
COPY requirements.txt /devops-challenge/requirements.txt
RUN pip install --no-cache-dir -r /devops-challenge/requirements.txt
EXPOSE 5000
CMD ["python", "./app/app.py"]