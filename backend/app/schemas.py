from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class PowerOutageCreate(BaseModel):
    location: str = Field(min_length=2, max_length=255)
    state: str = Field(min_length=2, max_length=100)

    started_at: datetime

    restored_at: datetime | None = None

    duration_minutes: float | None = Field(
        default=None,
        ge=0,
    )

    reported_by: str | None = Field(
        default=None,
        max_length=255,
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )

    @field_validator("restored_at")
    @classmethod
    def restoration_after_start(
        cls,
        restored_at: datetime | None,
        info,
    ):
        started_at = info.data.get("started_at")

        if (
            restored_at is not None
            and started_at is not None
            and restored_at < started_at
        ):
            raise ValueError(
                "restored_at cannot be earlier than started_at"
            )

        return restored_at


class PowerOutageResponse(PowerOutageCreate):
    id: int
    verified: bool

    model_config = ConfigDict(from_attributes=True)
