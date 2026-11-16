# marktmentor

Official Python SDK for the [MarktMentor Public API](https://api.marktmentor.nl):
bol product research and your own store data.

```python
import os

from marktmentor import MarktMentor
from marktmentor.errors import PaymentRequiredError

client = MarktMentor(token=os.environ["MARKTMENTOR_API_KEY"])

try:
    for product in client.products.list(search="drinkfles"):  # all pages
        print(product.product_code, product.title)
    history = client.products.sales_history("ean:8712345678901", period="1Y", interval="month")
except PaymentRequiredError as error:
    print("Allowance used up:", error.body.code)
```

Spending is limited by your account setting, not by the SDK: extra usage above
the bundle is off by default, and the organization owner sets a monthly maximum
in the dashboard. A used-up allowance gives `PaymentRequiredError`; `error.body.code`
is `bundle_exhausted`, `overage_limit_reached` or `free_quota_exhausted`. The
generated reference is in `src/marktmentor/reference.md`.
