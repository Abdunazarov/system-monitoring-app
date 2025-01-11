# stdlib
from contextlib import asynccontextmanager

# third-party
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession

# project
from db_setup import get_session, init_db
from services import get_system_metrics, record_system_usage, fetch_history

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    """Serve the main page."""
    return FileResponse("static/index.html")

@app.get("/metrics")
async def get_metrics():
    """Fetch system metrics in real-time."""
    return await get_system_metrics()

@app.post("/start-recording")
async def start_recording(db: AsyncSession = Depends(get_session)):
    """Record system usage data asynchronously."""
    await record_system_usage(db)
    return {"message": "Recording started"}

@app.get("/history")
async def get_history(db: AsyncSession = Depends(get_session)):
    """Retrieve past recorded data."""
    return await fetch_history(db)
