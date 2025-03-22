from typing import Any, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any, *args) -> str:
        if isinstance(v, ObjectId):
            return str(v)
        if isinstance(v, str) and ObjectId.is_valid(v):
            return v
        raise ValueError("Invalid ObjectId")


"""pydantic models for internal workings of the data"""
class GameCreate(BaseModel):
    name: str = Field(..., min_length=4)
    type: str = Field(..., min_length=4)
    publisher_name: str = Field(..., min_length=4)
    external_game_id: str = Field(..., min_length=1)
    description: str = Field(default="", min_length=0)
    is_featured: bool = Field(default=False)
    cover_image_url: str = Field(..., min_length=1)


class GameUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=4)
    type: Optional[str] = Field(None, min_length=4)
    publisher_name: Optional[str] = Field(None, min_length=4)
    external_game_id: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = Field(None, min_length=0)
    is_featured: Optional[bool] = Field(None)
    cover_image_url: Optional[str] = Field(None, min_length=1)


class GameResponse(GameCreate):
    id: PyObjectId = Field(alias="_id")
