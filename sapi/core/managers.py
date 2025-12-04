
from enum import Enum
import yaml
from typing import Protocol, Dict, List, Any
from abc import abstractmethod

from dotenv import load_dotenv
from os import listdir, getenv

class Manager(Protocol):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.routes_field = 'routes'

    @abstractmethod
    def routes(self) -> List:
        ...

class ManagerYaml(Manager):
    def __init__(self, filename: str) -> None:
        super().__init__(filename=filename)
        self.__configs = yaml.safe_load(open(self.filename, 'r'))
    
    def routes(self):
        return self.__configs.get(self.routes_field, [])

class ManagerJson(Manager):
    ...

class ManagerConf(Manager):
    ...

class ManagerToml(Manager):
    ...

class ManagerFactory:
    def __init__(self):
        self.filename = ''
        self.extension = ''
        if '.env' in listdir():
            load_dotenv(override=True)
            self.filename = getenv('config.filename', '')
            self.extension = self.filename.split('.', 1)[1]

    def create(self) -> Manager:
        match self.extension:
            case 'yaml': 
                return ManagerYaml(self.filename)
            case 'json':
                return ManagerJson(self.filename)
            case 'conf':
                return ManagerConf(self.filename)
            case 'toml':
                return ManagerToml(self.filename)
            case _:
                raise TypeError('invalid file extension!')
            