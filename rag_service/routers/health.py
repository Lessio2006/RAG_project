from fastapi import FastAPI, APIRouter, HTTPException


router = APIRouter(tags=['System', '💓'])

@router.get("/health")
def health_check():
    return {"status": "ok"}