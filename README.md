# database_setting

## Project Description

이 프로그램은 kream 서버에서 상품 데이터를 크롤링해와서 데이터베이스에 적재하고 판매 가격 더미데이터를 적재하는 프로그램 입니다.

## Program Structure

<img width="786" alt="image" src="https://user-images.githubusercontent.com/66009926/182016542-81bdf6b3-0636-4051-84b7-2e2462b0ff14.png">

## 프로그램 Action

### 1. Kream으로부터 상품 상세 페이지 url을 가져옵니다.

```
https://kream.co.kr/products/67945 
https://kream.co.kr/products/70263 
https://kream.co.kr/products/28029 
https://kream.co.kr/products/12831 
https://kream.co.kr/products/28030 
...
```
### 2. 상품 상세 페이지에서 브랜드명, 상품 영어명, 상품 한글명, 썸네일 urls를 가져옵니다.
이때, 각 데이터를 txt로 저정하기 위해 "---"로 구분하였고, 썸네일 urls는 " "(공백)으로 구분하였습니다.
```
Nike---(W) Nike Air Force 1 '07 Low Triple Black---(W) 나이키 에어포스 1 '07 로우 트리플 블랙---https://kream-phinf.pstatic.net/MjAyMjA0MTFfMjEz/MDAxNjQ5NjQ2MDU1Mzc4.O4WkytUI6pGbQ3vSAwW6N4OXLWj8GMsDcYv1IY2W5dwg.jvXzAqASaOEh4MocL3kuqEVgVJBvseWXovbItfIoZ7Mg.PNG/a_d8dc7818e7b24f4ab923f9c70ddb9b6e.png?type=l https://kream-phinf.pstatic.net/MjAyMjA0MTFfMjIy/MDAxNjQ5NjQ2MDU1Mzgw.KWvKSZDCgaD8mjOw3g6wZ30fcdr-P_wQBKNGKzSDLw0g.dUq9mrFzB8XOZDhha3IGVHHPYSiXDNrHhWRxSis72E8g.PNG/a_df0ec7f562804ac68bb6eef456389639.png?type=l https://kream-phinf.pstatic.net/MjAyMjA0MTFfMjcz/MDAxNjQ5NjQ2MDU1MzYx.jnr0N1yLIrinL0cpUcYdViDSg6dxJwcexg_uS6bilyAg.uNKWIwS_g4QtkU5-lcPNTbnK-cTTigrFQgT8mYMc3KYg.PNG/a_275d7ba7c9a14d2f8395ec5cd2ae0f8c.png?type=l https://kream-phinf.pstatic.net/MjAyMjA0MTFfODQg/MDAxNjQ5NjQ2MjI3NjIz.7rG-bayw60x9ss2wD-scNyClF3HE3oU2isXaWKLFlb0g.82OTWIo2gPnmq6AB92oG3YnpSTEKwr-b9g8zIe8tERsg.PNG/a_2f30f8095a4d434390f07d658aab2f6f.png?type=l
Nike---Nike Dunk Low Retro SE Next Nature Nike Sun Club---나이키 덩크 로우 레트로 SE 넥스트 네이쳐 나이키 썬 클럽---https://kream-phinf.pstatic.net/MjAyMjA0MjlfMjM2/MDAxNjUxMjI0MzY4Mzgx.DWz5fLEV6hx6jXtPeTU4m5K3qzPTxkhhcF_-WuLEoaAg.seGCw_RPmTFT5fZAvR5vLMM2suk7Z8oNT8OOHyCccCAg.PNG/a_381dd8eb2d1b48bea4388b1d40c3c1c6.png?type=l https://kream-phinf.pstatic.net/MjAyMjA0MjlfNDUg/MDAxNjUxMjI0MzcyOTkz.m4FJty8bo2i_xVmBH7Gp9O8Cntk3AdgYpM0DlEnIpaAg.TL5dX2tNuRfiYuUCqx_wi_3t_-5BPEtfTmmIVgvlqqsg.PNG/a_63f00ce6f48b45faaa17444d09476976.png?type=l https://kream-phinf.pstatic.net/MjAyMjA0MjlfMjAw/MDAxNjUxMjI0MzcyOTM0.st0bpNaE0Rp2gZ-o1WRjVFHoKwxO31dKXdCqLO4GeiIg._sm308kwjLZTpRGuhPyv8H7swFdkTWq0CncriUgRiL0g.PNG/a_825cdcd81da24814aa1449bf011e3345.png?type=l
Converse---Converse x Stussy One Star Ox Black---컨버스 x 스투시 원스타 로우 블랙---https://kream-phinf.pstatic.net/MjAyMjA2MDhfMjY1/MDAxNjU0NjUyNzc5MDk2.kM28f4jVrtWASCQhoi1cd4LZZFGSZI84WY96tkBpvsIg.wd087WlJ2pIGqx1zf2qtgcHREeu7bwqhZRr1kjXWdysg.PNG/a_eb015832612c40588a2ed1b5d795a73c.png?type=l https://kream-phinf.pstatic.net/MjAyMjA2MDhfMTc4/MDAxNjU0NjUyNzc5MTIy.xgS6imH5Ou6kFqNZg52p-RZuu8DuvTqrAtFYN-jWBKIg.C2KhmQz0GuJ6hby2R7uBKVUGgVB7mg6rGphtPZUdSV4g.PNG/a_d34eefe9e85647ec81ba1c0816359a1f.png?type=l https://kream-phinf.pstatic.net/MjAyMjA2MDhfODIg/MDAxNjU0NjUyNzc5MTQx.ujpcbvwe85QrFTIb4917biXojXyijGZc4VhcTrQhdJsg.b1d8rXfifc8lycx-oK8pPxWa8AquftknLqqE5owS3pMg.PNG/a_863b4b9daad542f4ac4bc7f0472fc3a7.png?type=l https://kream-phinf.pstatic.net/MjAyMjA2MDhfMjgz/MDAxNjU0NjUyNzc5MTAz.Dvls46e1m_U8RhItvZ6yDF53Rv6Zc35lGc72fAIWyi8g.Zz7f5ArezQ52fXwVapyX88m0B3ii-JVUetcVV01X8bEg.PNG/a_71457317a9e44381976e73a782c0d600.png?type=l
Converse---Converse x Play Comme des Garcons Chuck 70 Ox White---컨버스 x 플레이 꼼데가르송 척 70 로우 화이트---https://kream-phinf.pstatic.net/MjAyMDEwMjJfMTg1/MDAxNjAzMzM0MDAzMDUz.IP4WYoUBEImOS2VygeT6iH5OGElUQtJBEaBLD__v8bUg.zz03dgW0q2zV7QsWt2mXxZrrdQ7XHFoISAP13VGsnCQg.PNG/p_23510_0_f8389322aced42cead2e309687705da1.png?type=l
```
### 3. 받아온 상세 데이터를 SQL Archemy를 통해서 DB에 저장합니다.

``` python
# 상품 테이블
class Product(Base):
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    brand = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

# 썸네일 테이블
class Thumbnail(Base):
    __tablename__ = 'thumbnail'

    id = Column(BigInteger, primary_key=True)
    url = Column(String(255), nullable=False)
    product_id = Column(ForeignKey('product.id'), index=True)

    product = relationship('Product')
```
### 4. 저장한 상품데이터를 기반으로 Price Dummy Data를 적재합니다.
가격대 선정은 기본 금액 범위(100000 ~ 300000) * 가중치(1~9)이며 가중치는 랜덤입니다.
판매자는 admin 계정이며 신발 사이즈는 230 ~ 290까지 랜덤으로 부과됩니다.
상품 판매 개수 상품당 100 ~ 200 사이로 정해집니다.


```python
# Price 테이블
class Price(Base):
    __tablename__ = 'price'

    id = Column(BigInteger, primary_key=True)
    price = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    product_id = Column(ForeignKey('product.id'), index=True)
    seller_id = Column(ForeignKey('user.id'), index=True)

    product = relationship('Product')
    seller = relationship('User')
```

---
## Folder Structure

```
.
├── README.md
│
├── app.py
│
├── model
│   │
│   └── models.py
|
├── project_setting.py
│
├── resource
│   │
│   ├── product_data.txt # 상품 상세 데이터 임시 저장 txt
│   │
│   └── products_link_list.txt # 상품 상세 페이지 url 임시 저장 txt
│
├── service
│   |
│   ├── get_product_data.py # Step 2. 상품 상세 데이터를 가져오는 코드
|   |
│   ├── get_products_url_data.py # Step 1. 상품 상세 페이지 url을 가져오는 코드
|   |
│   ├── insert_price_database.py # Step 4. 데이터베이스에 상품 판매 더미 데이터를 넣는 코드
|   |
│   └── insert_product_thumbnail_database.py # Step 3. 상품 및 썸네일 데이터를 넣는 코드
|
└── tools
    |
    ├── SeleniumContextManager.py
    |
    └── SqlAlchemyContextManager.py
```

---
## How to run


### Requirement

```
Python : >= 3.10.1
```

### Project Setting

```python
# First, Set like below in project_setting.py

url_setting = {
    "mysql_url" : "mysql server url",
    "selenium_url" : "driver path",
}

INFINITE_SCROLL_COUNT = 5 # 무한 스크롤 중 몇 번을 스크롤 할 것인가

```

### Build Setup

```
python3 app.py
```
