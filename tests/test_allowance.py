"""HTTP 402 gives a typed error: the code is a fixed list in the schema."""

import httpx
import pytest

from marktmentor import MarktMentor
from marktmentor.errors import PaymentRequiredError


def client_with(status: int, body: dict) -> MarktMentor:
    transport = httpx.MockTransport(lambda request: httpx.Response(status, json=body))
    return MarktMentor(
        token="mm_test", base_url="https://api.test", httpx_client=httpx.Client(transport=transport)
    )


@pytest.mark.parametrize("code", ["bundle_exhausted", "overage_limit_reached", "free_quota_exhausted"])
def test_used_up_allowance_raises_payment_required_with_its_code(code):
    client = client_with(402, {"code": code, "detail": "Used up."})
    with pytest.raises(PaymentRequiredError) as raised:
        client.products.get("9300000012345678")
    assert raised.value.status_code == 402
    assert raised.value.body.code == code
