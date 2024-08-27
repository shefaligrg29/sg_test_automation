# Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    chromium-driver

CMD ["pytest", "-n", "4", "--html=reports/report.html"]
