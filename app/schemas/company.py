from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CompanyCreate(BaseModel):
    name : str
    description: Optional[str] = None
    website : Optional[str] = None
    location: Optional[str] = None

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    description : Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None

class CompanyResponse(BaseModel):
    id: int
    name: str
    descripttion: Optional[str]
    website: Optional[str]
    location: Optional[str]
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True