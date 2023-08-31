FROM python:3.10.8-slim
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80","main:app","--workers","1","-k","uvicorn.workers.UvicornWorker", "--timeout","1000"]