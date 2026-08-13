from sqlalchemy import create_engine

from app.models.models import Base
from app.db.session import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
