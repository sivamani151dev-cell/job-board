from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.application import ApplicationStatus

class ApplicationCreate(BaseModel):
    cover_letter: Optional[str] = None

class ApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus] = None

class ApplicationResponse(BaseModel):
    id: int
    cover_letter: Optional[str]
    status: ApplicationStatus
    created_at: datetime
    job_id: int
    applicant_id: int

    class Config: 
        from_attributes = True