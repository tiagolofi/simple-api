
import json
import yaml

from typing import Protocol, Dict, Any
from abc import abstractmethod
from os import listdir, getenv
from dotenv import load_dotenv

class Database(Protocol):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    @abstractmethod
    def get(self) -> Dict[str, Any]:
        ...

class DatabaseJson(Database):
    def __init__(self, filename: str) -> None:
        super().__init__(filename=filename)

    def get(self):
        ...

class DatabaseYaml(Database):
    def __init__(self, filename: str) -> None:
        super().__init__(filename=filename)
        self.data = yaml.safe_load(open(self.filename, 'r'))

    def get(self, key) -> Dict[str, Any]:
        return self.data.get(key, {})

class DatabaseFactory:
    def __init__(self):
        self.filename = ''
        self.extension = ''
        if '.env' in listdir():
            load_dotenv(override=True)
            self.filename = getenv('database.filename', '')
            self.extension = self.filename.split('.', 1)[1]

    def create(self) -> Database:
        match self.extension:
            case 'yaml':
                return DatabaseYaml(self.filename)
            case 'json':
                return DatabaseJson(self.filename)
            case _:
                raise TypeError('invalid file extension')
