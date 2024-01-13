from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class AbstractModel(BaseModel):
    id: UUID


class Persons(AbstractModel):
    name: str


class MovieModel(AbstractModel):
    title: str
    description: Optional[str] = None
    imdb_rating: Optional[float] = None
    genre: Optional[List[str]] = None
    director: Optional[List[str]] = None
    actors: Optional[List[Persons]] = None
    writers: Optional[List[Persons]] = None
    actors_names: Optional[List[str]] = None
    writers_names: Optional[List[str]] = None
