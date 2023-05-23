from datetime import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from project.models import Base


class AClass(Base):
    __tablename__ = 'a_class'
    id = Column(Integer, primary_key=True)
    insert_date = Column(Date)
    symbol = Column(String)
    pnu = Column(Float)
    projected_shares_outstanding = Column(Float)
    shares_outstanding = Column(Float)
    projected_nav = Column(Float)
    nav = Column(Float)
    basket_cash_per_currency = Column(JSONB)
    fund_cash_per_currency = Column(JSONB)
    info_type = Column(String)
    fund_family = Column(String)
    last_updated = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)