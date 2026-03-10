from typing import Annotated, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, Query, Path, Depends, Header, HTTPException, status
from query.teams import TeamQuery, TeamResponse
from query.events import EventQuery, EventResponse
from query.team_epas import TeamEpaRequest, TeamEpaResponse
from data.db import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
import data.models.teams as teams
import data.models.team_epas as team_epas

load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(
    api_key: Annotated[Optional[str], Header(alias="X-API-Key")] = None,
    db: Session = Depends(get_db)
):
    if not api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing API key")

    result = db.execute(
        text("SELECT 1 FROM users WHERE api_key = :api_key"),
        {"api_key": api_key}
    ).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "hello world!"}

@app.get("/teams", dependencies=[Depends(verify_api_key)])
async def get_teams(filter_query: Annotated[TeamQuery, Query()], db : Session = Depends(get_db)) -> TeamResponse:
    return teams.get_teams(db = db, query = filter_query)

@app.get("/events/{year}", response_model=EventResponse, dependencies=[Depends(verify_api_key)])
async def get_events(year : Annotated[int , Path(title="Events from this year")], query : Annotated[EventQuery, Query()]) -> EventResponse:
    return EventResponse(events=[], next=None)

@app.get("/team_epas/{team_number}", dependencies=[Depends(verify_api_key)])
async def get_team_epas(team_number : Annotated[int, Path(title="Team number")], query : Annotated[TeamEpaRequest, Query()], db : Session = Depends(get_db)) -> TeamEpaResponse:
    return team_epas.get_team_epa(db,team_number, query)

@app.get("/event_teams", dependencies=[Depends(verify_api_key)])
async def get_event_teams():
    pass
 
@app.get("/event_rankings", dependencies=[Depends(verify_api_key)])
async def get_event_rankings():
    pass

@app.get("/event_matches", dependencies=[Depends(verify_api_key)])
async def get_event_matches():
    pass

@app.get("/event_awards", dependencies=[Depends(verify_api_key)])
async def get_event_awards():
    pass

@app.get("/authorize", dependencies=[Depends(verify_api_key)])
async def authorize_user():
    return {"authorized": True}
