from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import INT, REAL
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class TeamEpa(Base):
    __tablename__ = "team_epas"

    team_number : Mapped[int] = mapped_column(INT, primary_key=True)
    year : Mapped[int] = mapped_column(INT, primary_key=True)
    normal_epa : Mapped[float] = mapped_column(REAL)
    epa : Mapped[float] = mapped_column(REAL)
    confidence : Mapped[float] = mapped_column(REAL)
    auto_epa : Mapped[float] = mapped_column(REAL)
    teleop_epa : Mapped[float] = mapped_column(REAL)
    endgame_epa : Mapped[float] = mapped_column(REAL)
    wins : Mapped[int] = mapped_column(INT)
    losses : Mapped[int] = mapped_column(INT)
    event_epa : Mapped[JSONB] = mapped_column(JSONB)
    ties : Mapped[int] = mapped_column(INT)

