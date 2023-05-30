from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    nonbinary = "nonbinary"

class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    id: Optional[UUID]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]