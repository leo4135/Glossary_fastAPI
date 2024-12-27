from pydantic import BaseModel

class TermBase(BaseModel):
    term: str
    description: str

class TermCreate(TermBase):
    pass

class TermUpdate(TermBase):
    pass

class TermInDB(TermBase):
    id: int

    class Config:
        orm_mode = True
