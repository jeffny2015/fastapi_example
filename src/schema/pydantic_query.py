from pydantic import BaseModel
from typing import List

class Query(BaseModel):
    query: str
    
class QueryResponse(Query):
    data: List | dict