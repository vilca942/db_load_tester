from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class Settings(BaseSettings):
    # Database configs
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "fake_db_password"
    db_database: str = "my_database"
    db_schema: str = "my_schema"

    @property
    def db_url(self) -> URL:
        """Database URL"""
        return URL.create(
            username=self.db_user,
            password=(
                None if self.db_password == "" else self.db_password
            ),  # Fixes CloudSQL Proxy Auth
            host=self.db_host,
            database=self.db_database,
            drivername="postgresql+psycopg2",
            port=self.db_port,
        )

    sentence_length: int = 50


settings = Settings()
