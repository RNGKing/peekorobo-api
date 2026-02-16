from typing import Annotated
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from query.teams import TeamQuery

load_dotenv()

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "hello world!"}

@app.get("/teams")
async def get_teams(filter_query: Annotated[TeamQuery, Query()]):
    return filter_query

@app.get("/events")
async def get_events():
    pass

@app.get("/team_epas")
async def get_team_epas():
    pass

@app.get("/event_teams")
async def get_event_teams():
    pass
 
@app.get("/event_rankings")
async def get_event_rankings():
    pass

@app.get("/event_matches")
async def get_event_matches():
    pass

@app.get("/event_awards")
async def get_event_awards():
    pass

@app.get("/authorize")
async def authorize_user():
    pass
