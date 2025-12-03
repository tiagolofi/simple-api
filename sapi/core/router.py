
import uuid

from fastapi import APIRouter
from typing import Dict
from importlib import import_module

from sapi.core.managers import Manager, Managers
from sapi.core.models import Request, Response

class Router(APIRouter):
    def __init__(self, manager: Managers) -> None:
        self.__init__(manager=manager.value)

    def __init__(self, manager: Manager) -> None:
        super().__init__()
        self.manager = manager

        for route in self.manager.routes():
            request, response, handler_fn = self.__load(route)

            # request será usado quando for necessário um wrapper para autenticação
            
            self.add_api_route(
                path=route.get('path'), 
                endpoint=handler_fn, 
                methods=[route.get('method')], 
                response_model=response,
            )

    def __load(self, route: Dict) -> tuple:
        class_name_req = route.get('request')
        class_name_res = route.get('response')
        handler_name = route.get('handler')
        module = import_module(route.get('package'))
        return getattr(module, class_name_req), getattr(module, class_name_res), getattr(module, handler_name)
