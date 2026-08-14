from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.models import PowerOutage
from app.schemas import PowerOutageCreate, PowerOutageResponse


router = APIRouter(
    prefix="/api/v1/outages",
    tags=["Outages"],
)


@router.post(
    "/",
    response_model=PowerOutageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_outage(
    outage: PowerOutageCreate,
    db: Session = Depends(get_db),
):
    new_outage = PowerOutage(**outage.model_dump())

    db.add(new_outage)
    db.commit()
    db.refresh(new_outage)

    return new_outage


@router.get(
    "/",
    response_model=list[PowerOutageResponse],
)
def get_outages(
    db: Session = Depends(get_db),
):
    outages = (
        db.query(PowerOutage)
        .order_by(PowerOutage.started_at.desc())
        .all()
    )

    return outages
