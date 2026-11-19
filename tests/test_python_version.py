"""The lowest Python version in pyproject.toml must really work.

On Python 3.9 every typed answer failed: Fern's serialization reads the type
hints of pydantic's own config, which use `X | None` (Python 3.10 syntax).
CI runs this file on the lowest supported version too.
"""

import httpx

from marktmentor import MarktMentor


def test_a_typed_answer_is_parsed():
    def handler(request):
        return httpx.Response(200, json=[{"id": 1, "name": "Example store"}])

    client = MarktMentor(
        token="mm_test",
        base_url="https://api.test",
        httpx_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    [organization] = client.organization.get()
    assert organization.name == "Example store"
