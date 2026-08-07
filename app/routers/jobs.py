from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.job import Job, JobType
from app.models.company import Company
from app.models.user import User
from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/jobs", tags="Jobs")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_access_token(token)
    if not username: 
        raise HTTPException(status_code=401, detail="Invalid or Expired token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/", response_model=JobResponse, status_code=201)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    company = db.query(Company).filter(
        Company.id == job.company_id,
        Company.owner_id == current_user.id
    ).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found or not yours")

    new_job = Job(
        title=job.title,
        description=job.description,
        requirements=job.requirements,
        salary_min=job.salary_min,
        salary_max=job.salary_max,
        location=job.location,
        job_type=job.job_type,
        company_id=job.company_id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    logger.info(f"Job created: {job.title} by {current_user.username}")
    return new_job

@router.get("/", response_model=list[JobResponse])
def get_jobs(
    keyword: Optional[str] = None,
    job_type: Optional[JobType] = None,
    location: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Job).filter(Job.is_active == True)

    if keyword:
        query = query.filter(Job.title.ilike(f"%{keyword}%"))
    if job_type:
        query = query.filter(Job.job_type == job_type)
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    offset = (page - 1) * limit
    jobs = query.offset(offset).limit(limit).all()
    return jobs

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    job_update: JobUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    company = db.query(Company).filter(
        Company.id == job.company_id,
        Company.owner_id == current_user.id
    ).first()
    if not company:
        raise HTTPException(status_code=403, detail="Not authorized to update this job")

    if job_update.title is not None:
        job.title = job_update.title
    if job_update.description is not None:
        job.description = job_update.description
    if job_update.requirements is not None:
        job.requirements = job_update.requirements
    if job_update.salary_min is not None:
        job.salary_min = job_update.salary_min
    if job_update.salary_max is not None:
        job.salary_max = job_update.salary_max
    if job_update.location is not None:
        job.location = job_update.location
    if job_update.job_type is not None:
        job.job_type = job_update.job_type
    if job_update.is_active is not None:
        job.is_active = job_update.is_active

    db.commit()
    db.refresh(job)
    logger.info(f"Job {job_id} updated by {current_user.username}")
    return job

@router.delete("/{job_id}", status_code=204)
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    company = db.query(Company).filter(
        Company.id == job.company_id,
        Company.owner_id == current_user.id
    ).first()
    if not company:
        raise HTTPException(status_code=403, detail="Not authorized to delete this job")

    db.delete(job)
    db.commit()
    logger.info(f"Job {job_id} deleted by {current_user.username}")
    return None