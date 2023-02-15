from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey
from sqlalchemy.ext.asyncio import AsyncSession
from schema.pydantic_query import Query, QueryResponse
from db.setup import async_get_db
from api.utils.query import raw_query
from utils import auth
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

router = APIRouter(
    prefix="/query"
)

@router.post("", response_model=QueryResponse, status_code=HTTP_200_OK)
async def execute_query(q: Query, db: AsyncSession = Depends(async_get_db), api_key: APIKey = Depends(auth.get_api_key) ):
    response = await raw_query(db=db, q=q)
    if response is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Something went wrong")
    return { "query" :  q.query, "data" : response}
