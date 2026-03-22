from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import setup_logging

# ADD THIS
from fastapi.middleware.cors import CORSMiddleware

setup_logging()

app = FastAPI(title="Africa LangGraph System")

# ADD THIS BLOCK (before routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
