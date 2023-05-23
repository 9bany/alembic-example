from datetime import datetime

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB

from project.models import Base


class BClass(Base):
    __tablename__ = 'b_class'
    id = Column(Integer, primary_key=True)