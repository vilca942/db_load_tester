from fastapi import FastAPI
from src.db_routes import router
from src.models import FastAPIInfo
from src.database import DB_ENGINE
from src.models import Base


def create_app() -> FastAPI:
    """init fastapi app fake commit"""

    app: FastAPI = FastAPI(
        title="database-load-tester",
        description="Backend to load test databases",
    )

    @app.get(path="/")
    def probe() -> FastAPIInfo:
        """root route for GCP probe"""

        return FastAPIInfo(
            name=app.title,
            description=app.description,
        )

    # attaching routes to the app
    app.include_router(router)

    # creating database tables
    Base.metadata.create_all(DB_ENGINE)

    return app


app = create_app()
