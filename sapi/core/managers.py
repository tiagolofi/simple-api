
from enum import Enum
import yaml
from typing import Protocol, Dict, List, Any
from abc import abstractmethod

from dotenv import load_dotenv
from os import listdir, getenv

class Manager(Protocol):
    def __init__(self) -> None:
        if '.env' in listdir():
            load_dotenv(override=True)
        self.filename = getenv('config.filename', '')
        self.extension = self.filename.split('.', 1)
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
    
    def routes(self):
        return self.__configs.get(self.routes_field, [])

class ManagerJson(Manager):
    ...

class ManagerConf(Manager):
    ...

class ManagerToml(Manager):
    ...

class Managers(Enum):
    YAML = ManagerYaml()
    JSON = ManagerJson()
    CONF = ManagerConf()
    TOML = ManagerToml()


class ManagerFactory:
    def __init__(self, manager: Manager):
        self.manager = manager

    def create(self) -> Managers:
        match self.manager.extension:
            case 'yaml': 
                return Managers.YAML
            case 'json':
                return Managers.JSON
            case 'conf':
                return Managers.CONF
            case 'toml':
                return Managers.TOML
            case _:
                raise TypeError('file extension invalid!')
