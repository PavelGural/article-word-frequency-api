from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models.article import Article
from .utils.file_reader import read_article
from .utils.text_processor import process_article, most_common_words

app = FastAPI()

class AnalyzeArticlesInput(BaseModel):
    articles: List[Article]
    n: int = 10

@app.post("/most_common_words")
def get_most_common_words(input_data: AnalyzeArticlesInput):
    words = []
    for article in input_data.articles:
        text = read_article(article.path)
        if text is None:
            raise HTTPException(status_code=404, detail=f"Article {article.name} not found")
        words.extend(process_article(text))
    return most_common_words(words, input_data.n)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
