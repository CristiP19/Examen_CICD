FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY app /app
#COPY app/static/images /app/static/images
COPY . .
EXPOSE 5000

CMD ["python", "app.py"]