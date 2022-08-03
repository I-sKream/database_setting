# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Product(Base):
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    brand = Column(String(255), nullable=False)
    name_eng = Column(String(255), nullable=False)
    name_kor = Column(String(255), nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(String(255), primary_key=True)
    nickname = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False, unique=True)


class Price(Base):
    __tablename__ = 'price'

    id = Column(BigInteger, primary_key=True)
    price = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    product_id = Column(ForeignKey('product.id'), index=True)
    seller_id = Column(ForeignKey('user.id'), index=True)

    product = relationship('Product')
    seller = relationship('User')


class Thumbnail(Base):
    __tablename__ = 'thumbnail'

    id = Column(BigInteger, primary_key=True)
    url = Column(String(255), nullable=False)
    product_id = Column(ForeignKey('product.id'), index=True)

    product = relationship('Product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(BigInteger, primary_key=True)
    date = Column(Date)
    buyer_id = Column(ForeignKey('user.id'), index=True)
    price_id = Column(ForeignKey('price.id'), index=True)

    buyer = relationship('User')
    price = relationship('Price')
