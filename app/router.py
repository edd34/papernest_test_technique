from fastapi import APIRouter, HTTPException
from app.apigouv import AdresseDataGouv
from app.helpers import get_coverage

router = APIRouter()

api_address_i = AdresseDataGouv()

@router.get("/coverage")
async def coverage(address: str):
    result_api_search = api_address_i.search(address)
    if result_api_search is None:
        raise HTTPException(status_code=500, detail="Server error")
    result_coverage = get_coverage(
        city=result_api_search["features"][0]["properties"]["city"],
    )
    if result_coverage is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": result_coverage}
