
import pytest
import app
from starlette.status import HTTP_200_OK
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_cat():
    headers = { "ACCESS_TOKEN" : "1234567" }
    async with AsyncClient(app=app.app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/cat", headers=headers)
        
    assert response.status_code == HTTP_200_OK
            