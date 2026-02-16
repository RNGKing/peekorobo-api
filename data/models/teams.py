from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class Teams(Base):
    __tablename__="teams"

    team_number : Mapped[int] = mapped_column(primary_key=True)
    nickname : Mapped[str] = mapped_column(Text)
    city : Mapped[str] = mapped_column(Text)
    state_prov : Mapped[str] = mapped_column(Text)
    country : Mapped[str] = mapped_column(Text)
    website : Mapped[str] = mapped_column(Text)
    district : Mapped[str] = mapped_column(Text)
