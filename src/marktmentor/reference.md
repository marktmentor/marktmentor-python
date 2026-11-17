# Reference
## Products
<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">list</a>(...) -> ProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search bol products by text, EAN, brand or category, with filters on sales, revenue, price and rating. Each result has the product data and the metrics per market for the chosen period.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.list(
    brand="Kambukka",
    ean="5407005143414",
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**brand:** `typing.Optional[str]` — Filter by brand name. The match is exact, upper and lower case included. Find the name with Search brands, or copy `brand` from a product.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — Filter by a bol category identifier. Find it with List categories, or copy it from `categories` of a product.
    
</dd>
</dl>

<dl>
<dd>

**ean:** `typing.Optional[str]` — Filter by a 13-digit EAN, including matching product variants.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ListProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**max_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_rating:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_revenue:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_sales:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_revenue:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_sales:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ListProductsRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for. In product lists, all words must match; the search also matches seller names, EANs and product codes. In review lists, each word must occur in the review text; upper and lower case do not matter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListProductsRequestSort]` 

* `sales` - sales
* `-sales` - -sales
* `revenue` - revenue
* `-revenue` - -revenue
* `price` - price
* `-price` - -price
    
</dd>
</dl>

<dl>
<dd>

**variants_of:** `typing.Optional[str]` — Return the other products in this product's family (its variants). Other filters and sorting still apply.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">get</a>(...) -> ProductDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one product by its bol product code, with the metrics per market for the chosen period, its dimensions, commission and the codes of its variants.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.get(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[GetProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[GetProductsRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">sales_history</a>(...) -> SalesHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the sales figures of a product over time, per market, in calendar buckets of the chosen interval.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.sales_history(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[SalesHistoryProductsRequestInterval]` 

Bucket size. With period=2Y, use month.

* `week` - week
* `month` - month
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[SalesHistoryProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[SalesHistoryProductsRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">visibility_history</a>(...) -> VisibilityHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the search visibility of a product over time, per market, in calendar buckets of the chosen interval.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.visibility_history(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[VisibilityHistoryProductsRequestInterval]` 

Bucket size. With period=2Y, use month.

* `week` - week
* `month` - month
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[VisibilityHistoryProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[VisibilityHistoryProductsRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">category_rankings</a>(...) -> CategoryRankingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the positions of a product in its bol categories over time.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.category_rankings(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[CategoryRankingsProductsRequestInterval]` 

Bucket size. With period=2Y, use month.

* `week` - week
* `month` - month
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[CategoryRankingsProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[CategoryRankingsProductsRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">keyword_rankings</a>(...) -> KeywordRankingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the positions of a product in the bol search results over time, per keyword and market. Name up to 25 keywords with keywordIds (the keywordId values of the keywords endpoint), or get the 10 keywords with the highest search volume.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.keyword_rankings(
    product_code="9300000138905032",
    keyword_ids="6797,6800,5150",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[KeywordRankingsProductsRequestInterval]` 

Bucket size. With period=2Y, use month.

* `week` - week
* `month` - month
    
</dd>
</dl>

<dl>
<dd>

**keyword_ids:** `typing.Optional[str]` — Up to 25 keywordId values from the keywords endpoint, separated by commas. Without it, the response has the 10 keywords of the keywords endpoint with the highest search volume in the last 30 days.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[KeywordRankingsProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[KeywordRankingsProductsRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">keywords</a>(...) -> KeywordResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the search terms a product ranked for in the period, with the figures per market.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.keywords(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[KeywordsProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[KeywordsProductsRequestPeriod]` 

* `7d` - 7d
* `30d` - 30d
* `90d` - 90d
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">sellers</a>(...) -> SellerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the sellers that offered a product in the period, with the figures per market, a buy box summary and the changes to the listing.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.sellers(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[SellersProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[SellersProductsRequestPeriod]` 

* `90d` - 90d
* `180d` - 180d
* `365d` - 365d
* `730d` - 730d
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">reviews</a>(...) -> ReviewListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the reviews of a product, with rating, text and date. Filter on score, verified purchase and text. By default the list has the reviews of the whole product family, as bol shows them on the product page; includeVariants=false gives only the reviews written for this product.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.reviews(
    product_code="9300000138905032",
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**include_variants:** `typing.Optional[bool]` — true (the default): also the reviews written for other variants of the same product family, as bol shows them on the product page. false: only the reviews written for this product. productCode of each review says for which product it was written.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ReviewsProductsRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ReviewsProductsRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**score:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for. In product lists, all words must match; the search also matches seller names, EANs and product codes. In review lists, each word must occur in the review text; upper and lower case do not matter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReviewsProductsRequestSort]` 

* `date` - date
* `-date` - -date
* `score` - score
* `-score` - -score
    
</dd>
</dl>

<dl>
<dd>

**verified:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/marktmentor/products/client.py">review_summary</a>(...) -> ReviewSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the review totals of a product: the number of reviews, the average rating, the count per star rating and the most named positive and negative topics. By default over the whole product family; includeVariants=false gives only the reviews written for this product.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.products.review_summary(
    product_code="9300000138905032",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_code:** `str` — Bol product identifier, returned as productCode. Or `ean:` with a 13-digit EAN, for example `ean:8712345678901`: the API then uses the product with that EAN. When more than one product has the EAN, the request gets HTTP 409 with the candidate product codes.
    
</dd>
</dl>

<dl>
<dd>

**include_variants:** `typing.Optional[bool]` — true (the default): also the reviews written for other variants of the same product family, as bol shows them on the product page. false: only the reviews written for this product. productCode of each review says for which product it was written.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Niches
<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">list</a>(...) -> NicheListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search niches by text or category. A niche is a group of products that serve the same customer need. Each result has the metrics per market for the chosen period.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.list(
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — Filter by a bol category identifier. Find it with List categories, or copy it from `categories` of a product.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ListNichesRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ListNichesRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for. In product lists, all words must match; the search also matches seller names, EANs and product codes. In review lists, each word must occur in the review text; upper and lower case do not matter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListNichesRequestSort]` 

* `revenue` - revenue
* `-revenue` - -revenue
* `volume` - volume
* `-volume` - -volume
* `products` - products
* `-products` - -products
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">get</a>(...) -> NicheDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one niche with its quality score, competition score and the metrics per market for the chosen period. With comparePeriods the response also has the core metrics for 30, 90 and 365 days.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.get(
    niche_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**compare_periods:** `typing.Optional[bool]` — Include core niche metrics for 30d, 90d and 365d in data.periods.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[GetNichesRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[GetNichesRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">review_history</a>(...) -> NicheHistoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the number of reviews and the average rating of the products in a niche over time.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.review_history(
    niche_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[ReviewHistoryNichesRequestInterval]` 

Bucket size. With period=2Y, use month.

* `week` - week
* `month` - month
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ReviewHistoryNichesRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ReviewHistoryNichesRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">review_summary</a>(...) -> ReviewSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the review totals of the products in a niche: the number of reviews, the average rating, the count per star rating and the most named positive and negative topics.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.review_summary(
    niche_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">product_distributions</a>(...) -> NicheDistributionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get how the products of a niche are spread over price, sales and revenue, for both markets together.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.product_distributions(
    niche_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ProductDistributionsNichesRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">products</a>(...) -> ProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the products in a niche, with the same filters and the same product data as Search products.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.products(
    niche_id=1,
    brand="Kambukka",
    ean="5407005143414",
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[str]` — Filter by brand name. The match is exact, upper and lower case included. Find the name with Search brands, or copy `brand` from a product.
    
</dd>
</dl>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — Filter by a bol category identifier. Find it with List categories, or copy it from `categories` of a product.
    
</dd>
</dl>

<dl>
<dd>

**ean:** `typing.Optional[str]` — Filter by a 13-digit EAN, including matching product variants.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ProductsNichesRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**max_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_rating:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_revenue:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**max_sales:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_price:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_revenue:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_sales:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ProductsNichesRequestPeriod]` 

* `30d` - 30d
* `90d` - 90d
* `365d` - 365d
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for. In product lists, all words must match; the search also matches seller names, EANs and product codes. In review lists, each word must occur in the review text; upper and lower case do not matter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ProductsNichesRequestSort]` 

* `sales` - sales
* `-sales` - -sales
* `revenue` - revenue
* `-revenue` - -revenue
* `price` - price
* `-price` - -price
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.niches.<a href="src/marktmentor/niches/client.py">reviews</a>(...) -> ReviewListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the reviews of the products in a niche. Filter on score, verified purchase and text.

A successful request counts as one research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.niches.reviews(
    niche_id=1,
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**niche_id:** `int` — Niche identifier returned as nicheId by Search niches.
    
</dd>
</dl>

<dl>
<dd>

**market:** `typing.Optional[ReviewsNichesRequestMarket]` — NL for the Netherlands, BE for Belgium, or ALL for both markets. Reviews support ALL only.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 25). A successful page counts as one request. For each query, page × pageSize must not be more than 10,000; make the query narrower with filters to reach other results.
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[ReviewsNichesRequestPeriod]` 

* `3M` - 3M
* `6M` - 6M
* `1Y` - 1Y
* `2Y` - 2Y
    
</dd>
</dl>

<dl>
<dd>

**score:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text to search for. In product lists, all words must match; the search also matches seller names, EANs and product codes. In review lists, each word must occur in the review text; upper and lower case do not matter.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReviewsNichesRequestSort]` 

* `date` - date
* `-date` - -date
* `score` - score
* `-score` - -score
    
</dd>
</dl>

<dl>
<dd>

**verified:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Reference
<details><summary><code>client.reference.<a href="src/marktmentor/reference/client.py">categories</a>(...) -> CategoryListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The bol category tree. Use it to find the `categoryId` for the product, niche and store filters. Send `level=1` for the top of the tree, `parentId` for the categories below one category, or `search` to find a category by name. Without a filter you get all categories, in the order of the tree.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.reference.categories(
    search="drinkfles",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**level:** `typing.Optional[int]` — Only categories of this level. Level 1 is the top of the tree.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 200).
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[int]` — Only the categories directly below this category.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Text in the category name. Every word must be in the name. Upper and lower case are the same.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reference.<a href="src/marktmentor/reference/client.py">category</a>(...) -> CategoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

One category with its level, its parent and its path. Use it to show the name and the path of a `categoryId` that you already have.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.reference.category(
    category_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `int` — Category identifier, returned as categoryId.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reference.<a href="src/marktmentor/reference/client.py">brands</a>(...) -> BrandListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Brand names that hold your search text, the brand with the most products first. The `brand` filter of a product search needs the exact name: copy it from this response.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.reference.brands(
    search="philips",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**search:** `str` — Text in the brand name, at least 2 characters. Upper and lower case are the same.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of brands (maximum 100).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/marktmentor/organization/client.py">get</a>() -> typing.List[Organization]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the organization that the credential belongs to. Use it to check which organization an API key or a portal connection reads.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.organization.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/marktmentor/usage/client.py">get</a>() -> Usage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the research requests of the organization in the current period: what the API bundle includes, what is used and what is left, or the state of the free monthly allowance. Use it to stop before the limit.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.usage.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Store
<details><summary><code>client.store.<a href="src/marktmentor/store/client.py">overview</a>(...) -> StoreOverviewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the revenue, costs, profit, orders, sales and returns of your own connected bol store for a period, compared with the period before.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.store.overview()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country:** `typing.Optional[OverviewStoreRequestCountry]` 

* `NL` - NL
* `BE` - BE
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.store.<a href="src/marktmentor/store/client.py">products</a>(...) -> StoreProductsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the products of your own connected bol store that had orders in the period, with sales, revenue, costs and profit per product.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.store.products()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category_id:** `typing.Optional[int]` — Only products in this bol category or in a category below it. The same identifier as `categoryId` in the research filters; find it with List categories.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[ProductsStoreRequestCountry]` 

NL or BE. Without this parameter: both countries.

* `NL` - NL
* `BE` - BE
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — The last N days, today included. Do not combine with startDate and endDate.
    
</dd>
</dl>

<dl>
<dd>

**eans:** `typing.Optional[str]` — EANs, separated by commas (maximum 100). With this filter, the page is in the sequence of sales (high to low) and `sort` only selects the products.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — Last day of the period (YYYY-MM-DD), included.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, from 1 to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 

Results per page: 5, 10, 25, 50 or 100.

* `5` - 5
* `10` - 10
* `25` - 25
* `50` - 50
* `100` - 100
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ProductsStoreRequestSort]` 

Sort field; a `-` prefix gives high to low. Selection and sequence use the order amounts before the final cost adjustments (advertising, storage, returns). Thus the sequence can be different from the sequence of `totalCosts` or `totalProfits`.

* `revenue` - revenue
* `-revenue` - -revenue
* `sales` - sales
* `-sales` - -sales
* `costs` - costs
* `-costs` - -costs
* `profits` - profits
* `-profits` - -profits
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — First day of the period (YYYY-MM-DD). Send it together with endDate. The period can be at most 366 days.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.store.<a href="src/marktmentor/store/client.py">inventory</a>(...) -> StoreInventoryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the active products of your own connected bol store with their stock and stock state.

This request is free: it does not count as a research request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from marktmentor import MarktMentor
from marktmentor.environment import MarktMentorEnvironment

client = MarktMentor(
    token="<token>",
    environment=MarktMentorEnvironment.PRODUCTION,
)

client.store.inventory(
    ean="5407005143414",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ean:** `typing.Optional[str]` — Only the product with this EAN.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Results per page (maximum 100).
    
</dd>
</dl>

<dl>
<dd>

**stock_state:** `typing.Optional[InventoryStoreRequestStockState]` 

out_of_stock: the stock is zero. low: the stock is 5 or less. ok: more than 5.

* `out_of_stock` - out_of_stock
* `low` - low
* `ok` - ok
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

