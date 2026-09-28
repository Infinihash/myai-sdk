import asyncio
import httpx
import myai
from myai import Client, MyAIClient


def test_client_alias_and_defaults():
    assert Client is MyAIClient
    c = Client(api_key="myai_test")
    assert c.base_url == "https://api.myaitoken.io"
    assert "10.0.0." not in c.base_url
    assert c._headers == {"Authorization": "Bearer myai_test"}
    assert "X-API-Key" not in c._headers
    assert myai.__version__ == "2.2.1"


def test_request_sends_bearer(monkeypatch):
    seen = {}

    async def fake_post(self, url, **kw):
        seen["url"] = url
        seen["headers"] = kw.get("headers")
        return httpx.Response(200, json={"id": "j1", "model": "m", "choices": [{"message": {"content": "hi"}}], "usage": {}},
                              request=httpx.Request("POST", url))

    monkeypatch.setattr(httpx.AsyncClient, "post", fake_post)
    r = asyncio.run(Client(api_key="myai_test").bid_and_execute(model="m", prompt="p"))
    assert r.output == "hi"
    assert seen["url"] == "https://api.myaitoken.io/v1/chat/completions"
    assert seen["headers"]["Authorization"] == "Bearer myai_test"
