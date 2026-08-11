from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, companies, jobs, applications
from fastapi.responses import RedirectResponse
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Board API",
    description="A backend API for job listings, companies and applications",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(companies.router)
app.include_router(jobs.router)
app.include_router(applications.router)

@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return RedirectResponse(url="/docs")