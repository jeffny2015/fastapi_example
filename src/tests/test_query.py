from fastapi.testclient import TestClient
from main import app
from starlette.status import HTTP_200_OK

class TestQuery:
    
    client: TestClient
    
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)
        
        
    def test_execute_query():
        response = client.post("/query")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {}
            