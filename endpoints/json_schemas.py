from pydantic import BaseModel


class Publication(BaseModel):
    userId: int
    id: int
    title: str
    body: str
