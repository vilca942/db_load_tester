from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from src.settings import settings

DB_ENGINE = create_engine(
    settings.db_url,
    pool_size=5,  # Max 5 connections per instance
    max_overflow=2,  # Allow 2 more connections to be created if pool is full
    pool_timeout=30,  # Wait 30 seconds before raising an error
    pool_recycle=1800,  # Recycle connections after 30 minutes
    pool_pre_ping=True,  # check if connection is alive before using it
    pool_use_lifo=True,  # Use LIFO for connection pool
)

SESSION_MAKER = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)


# Route dependency
def get_db_session():
    """dependency manages the db session closure"""

    db_session = SESSION_MAKER()
    try:
        yield db_session
    finally:
        db_session.close()
