from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PowerOutageCreate(BaseModel):
    location: str
    state: str
    started_at: datetime
    restored_at: datetime | None = None
    duration_minutes: float | None = None
    reported_by: str | None = None
    description: str | None = None


class PowerOutageResponse(PowerOutageCreate):
    id: int
    verified: bool

    model_config = ConfigDict(from_attributes=True)
