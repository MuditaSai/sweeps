from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from database import init_db, get_all_bonuses
from bonus_bot import claim_bonus

app = FastAPI()

init_db()

class BonusStatus(BaseModel):
    site: str
    last_claimed: Optional[str]
    balance: Optional[str]
    status: Optional[str]

@app.get("/status", response_model=List[BonusStatus])
def get_status():
    bonuses = get_all_bonuses()
    return [BonusStatus(site=b.site, last_claimed=b.last_claimed, balance=b.balance, status=b.status) for b in bonuses]

@app.post("/claim")
def manual_claim(site: str = Query(..., description="Site to claim bonus from")):
    try:
        claim_bonus(site)
        return {"message": f"Bonus claimed for {site}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
