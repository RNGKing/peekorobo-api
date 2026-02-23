from typing import List,Tuple
from pydantic import BaseModel

class EventAwardsResponse(BaseModel):
    event_key : str
    team_and_award : List[Tuple[int, str]]
