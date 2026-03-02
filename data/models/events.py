from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
from query.events import EventQuery, EventResponse, LocationInfo, EventMetaInfo

class Events(Base):
    __tablename__="events"

    event_key : Mapped[str] = mapped_column(Text, primary_key=True)
    name : Mapped[str] = mapped_column(Text)
    start_date: Mapped[str] = mapped_column(Text)
    end_date: Mapped[str] = mapped_column(Text)
    event_type: Mapped[str] = mapped_column(Text)
    city: Mapped[str] = mapped_column(Text)
    state_prov: Mapped[str] = mapped_column(Text)
    country: Mapped[str] = mapped_column(Text)
    website: Mapped[str] = mapped_column(Text)
    webcast_type: Mapped[str] = mapped_column(Text)
    webcast_channel: Mapped[str] = mapped_column(Text)
    distict_key: Mapped[str] = mapped_column(Text)
    distict_abbrev : Mapped[str] = mapped_column(Text)
    distict_name : Mapped[str] = mapped_column(Text)

def get_events(year : int, query : EventQuery) -> EventResponse:
    return EventResponse(
        events=[],
        next=None
    )
