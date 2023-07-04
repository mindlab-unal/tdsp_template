FROM python:3.11-slim

WORKDIR /app
COPY . /app
EXPOSE 8080 
RUN apt-get update && apt-get install  -y vim  && pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port", "8080"]

