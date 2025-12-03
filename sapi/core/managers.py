
from enum import Enum
import yaml
from typing import Protocol, Dict, List, Any
from abc import abstractmethod

class Manager(Protocol):
    def __init__(self) -> None:
        self.filename = "simple-api"
        self.configs_field = 'configs'
        self.auth_field = 'auth'
        self.routes_field = 'routes'

    @abstractmethod
    def configs(self) -> Dict|List|Any:
        ...

    @abstractmethod
    def auth(self) -> Dict|List|Any:
        ...

    @abstractmethod
    def routes(self) -> List:
        ...

class ManagerYaml(Manager):
    def __init__(self) -> None:
        super().__init__()
        self.__configs = yaml.safe_load(open(self.filename + '.yaml', 'r'))

    def configs(self):
        return self.__configs.get(self.configs_field, {})
    
    def auth(self):
        return self.__configs.get(self.auth_field, {})
    
    def routes(self):
        return self.__configs.get(self.routes_field, [])

class Managers(Enum):
    YAML = ManagerYaml()