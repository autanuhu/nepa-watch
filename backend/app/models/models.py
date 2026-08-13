from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PowerOutage(Base):
    __tablename__ = "power_outages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    location: Mapped[str] = mapped_column(String(255), index=True)
    state: Mapped[str] = mapped_column(String(100), index=True)

    started_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    restored_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    duration_minutes: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    reported_by: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
