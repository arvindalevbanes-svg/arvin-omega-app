from __future__ import annotations

from pathlib import Path
from typing import Optional
import shutil
import uuid

from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from engine_adapter import run_backtest, run_live

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="ARVIN Hybrid Server")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/backtest")
async def api_backtest(
    dataset: UploadFile = File(...),
    payout_name: Optional[str] = Form(default=None),
):
    suffix = Path(dataset.filename or "dataset.txt").suffix or ".txt"
    dataset_path = UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"
    with dataset_path.open("wb") as f:
        shutil.copyfileobj(dataset.file, f)

    result = run_backtest(str(dataset_path), payout_name)
    return JSONResponse(result)


@app.post("/api/live")
async def api_live(dataset: UploadFile = File(...)):
    suffix = Path(dataset.filename or "dataset.txt").suffix or ".txt"
    dataset_path = UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"
    with dataset_path.open("wb") as f:
        shutil.copyfileobj(dataset.file, f)

    result = run_live(str(dataset_path))
    return JSONResponse(result)
