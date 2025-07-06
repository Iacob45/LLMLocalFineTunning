from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import datetime as dt


ollamaModels = {0: 'llama2:latest',
                1: 'llama3.2:3b',
                2: 'qwen3:8b',
                3: 'gemma3:4b',
                4: 'deepseek-r1:8b',
                5: 'llama3.1:8b',
                6: 'mistral:7b',
                # 7: 'deepseek-r1:14b',
                # 8: 'deepseek-coder-v2:16b',
                # 9: 'gemma3:12b',
                # 10: 'gemma3:27b'
                }

class DataModel(BaseModel):
    name: str
    age: int
    birthday: dt.date
    gender: str = Field(description='Either M for male or F for female')

class Caption(BaseModel):
    string: str

class MovieGenreEnum(Enum):
    THRILLER = 'THRILLER'
    ACTION = 'ACTION'
    MYSTERY = 'MYSTERY'
    DRAMA = 'DRAMA'
    ROMANCE = 'ROMANCE'
    ANIMATION = 'ANIMATION'
    OTHER = 'OTHER'

class Movie(BaseModel):
    title: str
    release_year: int
    genres: List[MovieGenreEnum]

class MovieResponseModel(BaseModel):
    reasoning_text: str = Field(description='Explain in long detail why you decide exactly on these five movies.')
    recommended_movies: List[Movie]