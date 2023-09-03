# FastAPI Text Analysis API

A lightweight RESTful API for analyzing text documents and returning the most common words in the specified articles. The API is built using FastAPI and Python.

## Problem

The need to analyze text documents and extract useful information, such as the most common words, is a common task in natural language processing and text analytics.

## Solution

The FastAPI Text Analysis API provides a simple and efficient way to analyze text documents and return the most common words in the specified articles.

## Features

- Analyze multiple text documents at once
- Return the most common words in the specified articles
- Lightweight and fast, built using FastAPI and Python
- Easy to deploy and scale using Docker and Kubernetes

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Kubernetes
- Python library pytest
- Docker Scout

All commands below should be run from the root of the repo.

### Python UNIT testing

``` bash
pytest
========================= test session starts ======================
platform darwin -- Python 3.11.4, pytest-7.4.1, pluggy-1.3.0
rootdir: /Users/Pavel_Gural/git/PavelGural/fastapi-text-analysis
plugins: anyio-3.7.1
collected 3 items

src/app/tests/test_file_reader.py .                           [ 33%]
src/app/tests/test_text_processor.py ..                       [100%]

========================= 3 passed in 0.05s ========================
```

### Building the Docker Image

``` bash
docker build -t fastapi-text-analysis:1.0.0 .
```

### Docker vulnerability scanning

``` bash
docker scout cves pavelgural/fastapi-text-analysis:1.0.0
    ✓ SBOM of image already cached, 76 packages indexed
    ✓ No vulnerable package detected
```

### Running the Application

- Docker

``` bash
docker run -d --name fastapi-text-analysis --restart=always --pids-limit=1500 -p 5000:5000 -v "$(pwd)/article_examples:/article_examples" pavelgural/fastapi-text-analysis:1.0.0
```

- Docker Compose

``` bash
docker-compose up -d
```

- Kubernetes

``` bash
kubectl create configmap article-examples --from-file=article_examples/
kubectl apply -f k8s/fastapi-text-analysis.yaml
kubectl port-forward svc/fastapi-text-analysis 5000:5000
```

### Usage

Once the application is running, you can use a tool like curl or an API client like Postman to send a POST request to http://localhost:5000/most_common_words with a JSON payload containing the list of articles you want to analyze. For example:

``` bash
curl -X POST "http://localhost:5000/most_common_words" -H "Content-Type: application/json" -d '{
  "articles": [
    {
      "name": "Article 1",
      "path": "/article_examples/article1.txt"
    },
    {
      "name": "Article 2",
      "path": "/article_examples/article2.txt"
    },
    {
      "name": "Article 3",
      "path": "/article_examples/article3.txt"
    },
    {
      "name": "Article 4",
      "path": "/article_examples/article4.txt"
    }
  ],
  "n": 20
}'
["the","to","of","a","and","in","is","was","it","he","as","an","from","his","has","at","for","on","that","will"]
```

To analyze your own articles using the FastAPI Text Analysis API, simply add the article files to the `article_examples` folder and include them in the API request.

If you have a running application using Docker or Docker Compose, there is no need to restart the container to add them to the analysis, as the new articles will be automatically accessible. However, if you are using Kubernetes, you will need to update the ConfigMap and redeploy the application to make the new articles available to the running pods.

The number **20** in the API request represents the most common words to be returned from the specified articles.

### Removing the Application

- Docker:

``` bash
docker stop fastapi-text-analysis && docker rm fastapi-text-analysis
```

- Docker-compose:

``` bash
docker-compose down
```

- Kubernetes

``` bash
kubectl delete cm article-examples
kubectl delete -f k8s/fastapi-text-analysis.yaml
```
