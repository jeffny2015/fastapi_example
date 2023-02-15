from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.api_key import APIKey
from schema.pydantic_cat import Cat, CatResponse
from utils import auth
from starlette.status import HTTP_200_OK
from config import get_cat_settings, APICatSettings
from httpx import AsyncClient


router = APIRouter(
    prefix="/cat"
)

@router.get("", response_model=CatResponse, status_code=HTTP_200_OK)
async def get_cats(settings: APICatSettings = Depends(get_cat_settings), api_key: APIKey = Depends(auth.get_api_key)):
    print("hola")
    print(api_key)
    async with AsyncClient() as client:
        response = await client.get(url=settings.API_URI)
        r = response.json()
        
    if response.status_code != 200:
        response.raise_for_status()
    
    return { "data" : r}
