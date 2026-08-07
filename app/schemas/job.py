from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.job import JobType

class JobCreate(BaseModel):
    title: str
    description: str
    requirements: Optional[str] = None
    salary_max: Optional[float] = None
    salary_min: Optional[float] = None
    location: Optional[str] = None
    job_type: JobType = JobType.full_time
    company_id: int

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    location: Optional[str] = None
    job_type: Optional[JobType] = None
    is_active: Optional[bool] = None

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    requirements: Optional[str]
    salary_min: Optional[float]
    salary_max: Optional[float]
    location: Optional[str]
    job_type: JobType
    is_active: bool
    created_at: datetime
    company_id: int

    class Config:
        from_attributes = True