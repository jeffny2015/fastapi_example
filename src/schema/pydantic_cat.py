from typing import List
from pydantic import BaseModel

class Cat(BaseModel):
    ...

class CatResponse(Cat):
    data: List | dict