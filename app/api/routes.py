from fastapi import APIRouter
from app.schemas.request import QueryRequest
from app.graph.graph import graph

router = APIRouter()

@router.post("/query")
def query(req: QueryRequest):
    result = graph.invoke({"query": req.query})
    return {"response": result["final"]}