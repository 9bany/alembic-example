from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://root:secret@localhost:5432/migration')
