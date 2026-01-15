from pydantic import BaseModel, Field


class InfoModel(BaseModel):
    name: str
    location:str
    danger_rate: int = Field(...,ge=1,le=10)

