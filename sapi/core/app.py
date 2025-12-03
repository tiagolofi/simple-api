
from fastapi import FastAPI

from sapi.core.managers import Manager, Managers
from sapi.core.router import Router

class SimpleApi(FastAPI):

    def __init__(self, manager: Manager|Managers, prefix: str = ''):
        super().__init__()
        if isinstance(manager, Managers): # deve ser implementada com prioridade (python eu te odeio)
            self.api_router = Router(manager.value)
        elif isinstance(manager, Manager):
            self.api_router = Router(manager)
        else:
            raise TypeError('Invalid type Manager...')

        self.prefix = prefix

        self.include_router(self.api_router, prefix = self.prefix)

