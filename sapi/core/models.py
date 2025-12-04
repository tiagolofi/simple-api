
import uuid
from pydantic import BaseModel

class SimpleRequest(BaseModel):
    id: uuid.UUID

class SimpleResponse(BaseModel):
    id: uuid.UUID