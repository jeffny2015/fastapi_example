from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN
from config import AuthSettings, get_auth_settings

api_key_header = APIKeyHeader(name="RPA_TOKEN", auto_error=False)


async def get_api_key(settings: AuthSettings = Depends(get_auth_settings), api_key_header: str = Security(api_key_header)):
    print("enter")
    if api_key_header == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )