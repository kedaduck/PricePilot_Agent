# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from main import query_price

app = FastAPI(title="PricePilot Agent API")

class QueryRequest(BaseModel):
    query: str

@app.post("/compare")
def compare_price(request: QueryRequest):
    result = query_price(request.query)
    return {"result": result}

# 启动命令: uvicorn app:app --reload