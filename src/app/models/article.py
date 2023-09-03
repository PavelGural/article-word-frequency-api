from pydantic import BaseModel

class Article(BaseModel):
    name: str
    path: str
