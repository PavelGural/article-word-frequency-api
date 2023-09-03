# Use the smallest official Python base image (based on Alpine Linux)
FROM python:3.10-alpine

# Set environment variables PYTHONDONTWRITEBYTECODE and PYTHONUNBUFFERED to prevent writing .pyc files and to ensure that Python output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

RUN apk add --no-cache curl && \
    apk del --no-cache

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/app /app/src/app

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD curl --fail http://localhost:5000/health || exit 1

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "5000"]
