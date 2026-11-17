"""Final answers are not retried: 402 (allowance) and 409 (ambiguous EAN).

A 409 carries the candidate products; asking again gives the same answer after
the retry wait. 429 and 5xx are retried, like the other SDKs.
"""

import httpx
import pytest

from marktmentor import MarktMentor
from marktmentor.core.api_error import ApiError


def counting_client(status: int, body: dict):
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(status, json=body, headers={"Retry-After": "0"})

    client = MarktMentor(
        token="mm_test",
        base_url="https://api.test",
        httpx_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    return client, calls


@pytest.mark.parametrize(
    "status,body",
    [
        (402, {"code": "bundle_exhausted", "detail": "Used up."}),
        (409, {"code": "ambiguous_ean", "detail": "More products.", "candidates": []}),
    ],
)
def test_final_answers_are_sent_once(status, body):
    client, calls = counting_client(status, body)
    with pytest.raises(ApiError):
        client.products.get("ean:8712345678901")
    assert len(calls) == 1


@pytest.mark.parametrize("status", [429, 503])
def test_transient_answers_are_retried(status):
    client, calls = counting_client(status, {"code": "x", "detail": "Wait."})
    with pytest.raises(ApiError):
        client.products.get("9300000012345678")
    assert len(calls) == 3  # first try and 2 retries (default)
