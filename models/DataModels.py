from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
import datetime as dt


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
    reasoning_text = str = Field(description='Explain in long detail why you decide exactly on these five movies.')
    recommended_movies: List[Movie]