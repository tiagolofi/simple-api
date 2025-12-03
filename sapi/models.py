
import uuid
from pydantic import BaseModel

class Request(BaseModel):
    id: uuid.UUID

class Response(BaseModel):
    id: uuid.UUID