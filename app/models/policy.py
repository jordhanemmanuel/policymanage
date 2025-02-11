from typing import Literal, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, validator
from uuid import UUID, uuid4

class PolicyPut(BaseModel):
    customer_name: Optional[str] = None
    policy_type: Optional[Literal['auto', 'home']] = None
    expiry_date: Optional[datetime] = None
    
    @validator("expiry_date")
    def block_past_date(cls, v):
        if (v is None):
            return v
        if (v < datetime.now()):
            raise ValueError("Date cannot be in the past")
        return v

class PolicyBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    customer_name: str
    policy_type: Literal['auto', 'home']
    expiry_date: datetime
    
    @validator("expiry_date")
    def block_past_date(cls, v):
        date_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if (v < date_now):
            raise ValueError("Date cannot be in the past")
        return v

class Policy(PolicyBase):
    policy_id: UUID = Field(default_factory=uuid4)