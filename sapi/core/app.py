
from fastapi import FastAPI

from sapi.core.managers import ManagerFactory
from sapi.core.router import Router

class SimpleApi(FastAPI):

    def __init__(self, prefix: str = ''):
        super().__init__()
        self.api_router = self.__set_api_router()
        self.prefix = prefix
        self.include_router(self.api_router, prefix = self.prefix)

    def __set_api_router(self) -> Router:
        manager_factory = ManagerFactory()
        manager = manager_factory.create()
        return Router(manager)
