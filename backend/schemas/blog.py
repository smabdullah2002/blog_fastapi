from pydantic import BaseModel, root_validator
from datetime import datetime
from typing import Optional


class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if not values.get("slug") and values.get("title"):
            values["slug"] = values["title"].replace(" ", "-").lower()
        return values


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
