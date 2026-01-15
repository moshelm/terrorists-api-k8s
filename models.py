from pydantic import BaseModel, Field
from pymongo import MongoClient
from typing import Annotated, Optional
from pydantic import BeforeValidator, ConfigDict, Field,BaseModel

PyObjectId = Annotated[str,BeforeValidator(str)]


class BasicInfoTerrorist(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    location:str
    danger_rate: int = Field(...,ge=1,le=10)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        extra='ignore'
        )

class TopThreatsResponse(BaseModel):
    count: int
    top: list[BasicInfoTerrorist]

