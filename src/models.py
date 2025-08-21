from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text
from pydantic import BaseModel
from src.settings import settings


class Base(DeclarativeBase):
    pass


class Sentence(Base):
    """Sentence model"""

    __tablename__ = "sentences"
    __table_args__ = {
        "schema": f"{settings.db_schema}",
    }

    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(Text, nullable=False)


class FastAPIInfo(BaseModel):
    """Pydantic model for the probe route"""

    name: str
    description: str
